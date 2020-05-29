from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from numpy_fracdiff.frac_weights import frac_weights
from numpy_fracdiff.find_truncation import find_truncation
from numpy_fracdiff.apply_weights import apply_weights


class FracDiff(BaseEstimator, TransformerMixin):
    """Fractal Difference

    Apply fractal differencing on time-homogenous time series.

    Parameters
    ----------
    X : np.array
        Time series values. The time series are of  of ascending order (oldest
        first, latest last).

    y : default=None
        not used

    order : float or list of float, default=1.0
        Fractal order

    weights : list or list of lists, default=None
        Precomputed weighting scheme for the given fractal order.
        - `len(weights)==truncation`
        - It's the ouput of `numpy_fracdiff.frac_weights`

    truncation : int or list of int, default=None
        Truncation order or 'window'. How many past observations are used to
        compute one fractal difference value.
        - `len(weights)==truncation`
        - It's used in `numpy_fracdiff.frac_weights` to limit the for loop.

    tau : float, default=1e-5
        The acceptable truncation error to determine the truncation order.
        - It's used for the stopping criteria in
            `numpy_fracdiff.find_truncation`
        - Set `truncation=k-1´ if `|weight_k| < tau´

    mmax : int, default=20000
        The upper bound for backtracking the truncation order.
        - It limits the for loop in `numpy_fracdiff.find_truncation`

    dtype : np.dtype, default=None
        Return another data type, e.g., np.float32

    """
    def __init__(self, order: float = 1.0, weights: list = None,
                 truncation: int = None, tau: float = 1e-5, mmax: int = 20000,
                 dtype=None):
        # error checking
        if order is None:
            raise Exception('order must be a real positive number d>0')
        # store attributes
        self.order = order
        self.weights = weights
        self.truncation = truncation
        self.tau = tau
        self.mmax = mmax
        self.dtype = dtype

    def fit(self, X: np.ndarray, y=None):
        # determine weights
        if self.weights is None:
            if isinstance(self.truncation, int):
                self.weights = frac_weights(self.order, self.truncation)
            else:  # 'find' or None
                self.truncation, self.weights = find_truncation(
                    self.order, tau=self.tau, mmax=self.mmax)
        self.weights = np.array(self.weights)

        # enforce float data type
        if self.dtype is None:
            self.dtype = X[0].dtype if isinstance(X[0], float) else float

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        # multiply weights with lagged feature x
        if len(X.shape) == 1:
            Z = apply_weights(X.astype(self.dtype), self.weights)
        else:
            Z = np.empty(shape=X.shape)
            for j in range(X.shape[1]):
                Z[:, j] = apply_weights(
                    X[:, j].astype(self.dtype), self.weights)
        return Z

    # def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
    #    pass  # return X
