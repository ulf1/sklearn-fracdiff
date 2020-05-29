from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from numpy_fracdiff.frac_weights import frac_weights
from numpy_fracdiff.find_truncation import find_truncation
from numpy_fracdiff.apply_weights import apply_weights
from typing import List
from six.moves import collections_abc
import warnings


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

    order : float or List[float], default=1.0
        Fractal order

    truncation : int or List[int], default=None
        Truncation order or 'window'. How many past observations are used to
        compute one fractal difference value.
        - `len(weights)==truncation`
        - It's used in `numpy_fracdiff.frac_weights` to limit the for loop.

    weights : list or List[List[float]], default=None
        Precomputed weighting scheme for the given fractal order.
        - `len(weights)==truncation`
        - It's the ouput of `numpy_fracdiff.frac_weights`

    tau : float, default=1e-5
        The acceptable truncation error to determine the truncation order.
        - It's used for the stopping criteria in
            `numpy_fracdiff.find_truncation`
        - Set `truncation=k-1´ if `|weight_k| < tau´

    mmax : int, default=20000
        The upper bound for backtracking the truncation order.
        - It limits the for loop in `numpy_fracdiff.find_truncation`

    chop : str or int, default=None
        Method how to trim NaNs
        - None (default)
        - 'truncation' -- trims max(self.truncation) rows
        - 'mmax' -- trims self.mmax rows. It gives more control
        - int -- specify the number of rows to trim

    dtype : np.dtype, default=None
        Return another data type, e.g., np.float32

    """
    def __init__(self,
                 order: List[float] = None,
                 truncation: List[int] = None,
                 weights: List[List[float]] = None,
                 tau: float = 1e-5,
                 mmax: int = 20000,
                 chop: str = None,
                 dtype=None):
        # store attributes
        self.order = order
        self.weights = weights
        self.truncation = truncation
        self.tau = tau
        self.mmax = mmax
        self.chop = chop
        self.dtype = dtype
        self.n_features = None

    def fit(self, X: np.ndarray, y=None):
        # store the number of features
        self.n_features = 1 if len(X.shape) == 1 else X.shape[1]

        # convert self.order to list
        if isinstance(self.order, (float, int)):
            self.order = [self.order for _ in range(self.n_features)]
        # convert self.truncation to list
        if isinstance(self.truncation, (float, int)):
            self.truncation = [self.truncation for _ in range(self.n_features)]
        # convert self.weights to List[List]
        if isinstance(self.weights, collections_abc.Iterable):
            if not isinstance(self.weights[0], collections_abc.Iterable):
                self.weights = [
                    np.array(self.weights) for _ in range(self.n_features)]

        # limit mmax to X
        self.mmax = min(len(X), self.mmax)

        # determine weights
        if self.weights is None:
            if isinstance(self.truncation, collections_abc.Iterable):
                self.weights = [
                    np.array(frac_weights(o, m)) for o, m
                    in zip(self.order, self.truncation)]
            else:  # None
                self.truncation = []
                self.weights = []
                for o in self.order:
                    m, w = find_truncation(o, tau=self.tau, mmax=self.mmax)
                    self.truncation.append(m)
                    self.weights.append(np.array(w))

        # determine truncation
        if self.truncation is None:
            self.truncation = [len(w) for w in self.weights]

        # enforce float data type
        if self.dtype is None:
            self.dtype = X[0].dtype if isinstance(X[0], float) else float

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        # warning if X is too short
        if len(X) < max(self.truncation):
            warnings.warn((
                f"len(X)={len(X)} is too short for the truncation order "
                f"m={max(self.truncation)}"))
        # multiply weights with lagged feature x
        if len(X.shape) == 1:
            Z = apply_weights(X.astype(self.dtype), self.weights[0])
        else:
            Z = np.empty(shape=X.shape)
            for j in range(self.n_features):
                Z[:, j] = apply_weights(
                    X[:, j].astype(self.dtype), self.weights[j])
        # chop NaN rows
        if isinstance(self.chop, int):
            Z = Z[self.chop:]
        elif isinstance(self.chop, str):
            if self.chop == 'mmax':
                Z = Z[self.mmax:]
            elif self.chop == 'truncation':
                Z = Z[max(self.truncation):]
        # done
        return Z

    # def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
    #    pass  # return X
