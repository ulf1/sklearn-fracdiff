from sklearn_fracdiff.fracdiff_class import FracDiff
import numpy as np
import numpy.testing as npt


def test1():
    x = np.array([10, 11, 9])
    w = [1.0, -1.0]
    z = FracDiff(weights=w).fit_transform(x)
    target = np.array([np.nan, 1.0, -2.0])
    npt.assert_allclose(z, target)


def test2():
    x = np.array([10, 11, 9])
    w = [1.0, -2.0, 1.0]
    z = FracDiff(weights=w).fit_transform(x)
    target = np.array([np.nan, np.nan, -3.0])
    npt.assert_allclose(z, target)


def test3():
    x = np.array([10, 11, 9])
    z = FracDiff(order=1, truncation='find').fit_transform(x)
    target = np.array([np.nan, 1.0, -2.0])
    npt.assert_allclose(z, target)


def test4():
    x = np.array([10, 11, 9])
    z = FracDiff(order=2, truncation='find').fit_transform(x)
    target = np.array([np.nan, np.nan, -3.0])
    npt.assert_allclose(z, target)


def test5():
    x = np.array([10, 11, 9])
    z = FracDiff(order=1, truncation=1).fit_transform(x)
    target = np.array([np.nan, 1.0, -2.0])
    npt.assert_allclose(z, target)


def test6():
    x = np.array([10, 11, 9])
    z = FracDiff(order=2, truncation=2).fit_transform(x)
    target = np.array([np.nan, np.nan, -3.0])
    npt.assert_allclose(z, target)


def test7():
    x = np.array([10, 11, 9])
    z = FracDiff(order=1).fit_transform(x)
    target = np.array([np.nan, 1.0, -2.0])
    npt.assert_allclose(z, target)


def test8():
    x = np.array([10, 11, 9])
    z = FracDiff(order=2).fit_transform(x)
    target = np.array([np.nan, np.nan, -3.0])
    npt.assert_allclose(z, target)


def test11():
    X = np.array([[10, 11, 9], [4, 6, 9]]).T
    Z = FracDiff(order=1).fit_transform(X)
    target = np.array([[np.nan, 1.0, -2.0], [np.nan, 2.0, 3.0]]).T
    npt.assert_allclose(Z, target)
