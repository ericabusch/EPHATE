import numbers
import warnings
from deprecated import deprecated
import numpy as np
from . import matrix

try:
    import pandas as pd
except ImportError:  # pragma: no cover
    # pandas not installed
    pass

try:
    import anndata
except ImportError:  # pragma: no cover
    # anndata not installed
    pass


def is_DataFrame(X):
    try:
        return isinstance(X, pd.DataFrame)
    except NameError:  # pragma: no cover
        # pandas not installed
        return False

def is_Symmetric(X,tol=1e-08):
    if X.shape[0]!=X.shape[1]: return False
    return np.allclose(X,X.T,rtol=tol,atol=tol)

def row_normalize(M):
    """
    Row-normalizes a given matrix.

    Parameters:
    M (np.ndarray): The matrix to be row-normalized.

    Returns:
    np.ndarray: The row-normalized matrix.
    """

    if check_row_normalize(M):
        return M

    row_sums = M.sum(axis=1, keepdims=True)
    # Avoid division by zero by replacing zero sums with one
    row_sums[row_sums == 0] = 1
    # Normalize each row by its sum
    normalized_matrix = M / row_sums
    return normalized_matrix

def check_row_normalize(M):
    return np.allclose(M.sum(axis=1), 1)

def is_SparseDataFrame(X):
    try:
        pd
    except NameError:  # pragma: no cover
        # pandas not installed
        return False
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            "The SparseDataFrame class is removed from pandas. Accessing it from the top-level namespace will also be removed in the next version",
            FutureWarning,
        )
        try:
            return isinstance(X, pd.SparseDataFrame)
        except AttributeError:
            return False


def is_Anndata(X):
    try:
        return isinstance(X, anndata.AnnData)
    except NameError:  # pragma: no cover
        # anndata not installed
        return False


def check_greater(x, **params):
    """Check that parameters are greater than x as expected

    Parameters
    ----------

    x : excepted boundary
        Checks not run if parameters are greater than x 

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if not isinstance(params[p], numbers.Number) or params[p] <= x:
            raise ValueError("Expected {} > {}, got {}".format(p, x, params[p]))


def check_positive(**params):
    """Check that parameters are positive as expected

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    return check_greater(0, **params)


def check_int(**params):
    """Check that parameters are integers as expected

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if not isinstance(params[p], numbers.Integral):
            raise ValueError("Expected {} integer, got {}".format(p, params[p]))


def check_if_not(x, *checks, **params):
    """Run checks only if parameters are not equal to a specified value

    Parameters
    ----------

    x : excepted value
        Checks not run if parameters equal x

    checks : function
        Unnamed arguments, check functions to be run

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if params[p] is not x and params[p] != x:
            [check(**{p: params[p]}) for check in checks]


def check_in(choices, **params):
    """Checks parameters are in a list of allowed parameters

    Parameters
    ----------

    choices : array-like, accepted values

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if params[p] not in choices:
            raise ValueError(
                "{} value {} not recognized. Choose from {}".format(
                    p, params[p], choices
                )
            )


def check_between(v_min, v_max, **params):
    """Checks parameters are in a specified range

    Parameters
    ----------

    v_min : float, minimum allowed value (inclusive)

    v_max : float, maximum allowed value (inclusive)

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    check_greater(v_min, v_max=v_max)
    for p in params:
        if params[p] < v_min or params[p] > v_max:
            raise ValueError(
                "Expected {} between {} and {}, "
                "got {}".format(p, v_min, v_max, params[p])
            )


@deprecated(version="1.5.0", reason="Use graphtools.matrix.if_sparse instead")
def if_sparse(*args, **kwargs):
    return matrix.if_sparse(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.sparse_minimum instead")
def sparse_minimum(*args, **kwargs):
    return matrix.sparse_minimum(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.sparse_maximum instead")
def sparse_maximum(*args, **kwargs):
    return matrix.sparse_maximum(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.elementwise_minimum instead")
def elementwise_minimum(*args, **kwargs):
    return matrix.elementwise_minimum(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.elementwise_maximum instead")
def elementwise_maximum(*args, **kwargs):
    return matrix.elementwise_maximum(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.dense_set_diagonal instead")
def dense_set_diagonal(*args, **kwargs):
    return matrix.dense_set_diagonal(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.sparse_set_diagonal instead")
def sparse_set_diagonal(*args, **kwargs):
    return matrix.sparse_set_diagonal(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.set_diagonal instead")
def set_diagonal(*args, **kwargs):
    return matrix.set_diagonal(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.set_submatrix instead")
def set_submatrix(*args, **kwargs):
    return matrix.set_submatrix(*args, **kwargs)


@deprecated(
    version="1.5.0", reason="Use graphtools.matrix.sparse_nonzero_discrete instead"
)
def sparse_nonzero_discrete(*args, **kwargs):
    return matrix.sparse_nonzero_discrete(*args, **kwargs)


@deprecated(
    version="1.5.0", reason="Use graphtools.matrix.dense_nonzero_discrete instead"
)
def dense_nonzero_discrete(*args, **kwargs):
    return matrix.dense_nonzero_discrete(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.nonzero_discrete instead")
def nonzero_discrete(*args, **kwargs):
    return matrix.nonzero_discrete(*args, **kwargs)


@deprecated(version="1.5.0", reason="Use graphtools.matrix.to_array instead")
def to_array(*args, **kwargs):
    return matrix.to_array(*args, **kwargs)


@deprecated(
    version="1.5.0", reason="Use graphtools.matrix.matrix_is_equivalent instead"
)
def matrix_is_equivalent(*args, **kwargs):
    return matrix.matrix_is_equivalent(*args, **kwargs)


# below are the phate utils
import numbers
import numpy as np


def check_positive(**params):
    """Check that parameters are positive as expected

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if not isinstance(params[p], numbers.Number) or params[p] <= 0:
            raise ValueError("Expected {} > 0, got {}".format(p, params[p]))


def check_int(**params):
    """Check that parameters are integers as expected

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if not isinstance(params[p], numbers.Integral):
            raise ValueError("Expected {} integer, got {}".format(p, params[p]))


def check_if_not(x, *checks, **params):
    """Run checks only if parameters are not equal to a specified value

    Parameters
    ----------

    x : excepted value
        Checks not run if parameters equal x

    checks : function
        Unnamed arguments, check functions to be run

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if params[p] is not x and params[p] != x:
            [check(**{p: params[p]}) for check in checks]


def check_in(choices, **params):
    """Checks parameters are in a list of allowed parameters

    Parameters
    ----------

    choices : array-like, accepted values

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if params[p] not in choices:
            raise ValueError(
                "{} value {} not recognized. Choose from {}".format(
                    p, params[p], choices
                )
            )


def check_between(v_min, v_max, **params):
    """Checks parameters are in a specified range

    Parameters
    ----------

    v_min : float, minimum allowed value (inclusive)

    v_max : float, maximum allowed value (inclusive)

    params : object
        Named arguments, parameters to be checked

    Raises
    ------
    ValueError : unacceptable choice of parameters
    """
    for p in params:
        if params[p] < v_min or params[p] > v_max:
            raise ValueError(
                "Expected {} between {} and {}, "
                "got {}".format(p, v_min, v_max, params[p])
            )


def matrix_is_equivalent(X, Y):
    """
    Checks matrix equivalence with numpy, scipy and pandas
    """
    return X is Y or (
        isinstance(X, Y.__class__)
        and X.shape == Y.shape
        and np.sum((X != Y).sum()) == 0
    )


def in_ipynb():
    """Check if we are running in a Jupyter Notebook

    Credit to https://stackoverflow.com/a/24937408/3996580
    """
    __VALID_NOTEBOOKS = [
        "<class 'google.colab._shell.Shell'>",
        "<class 'ipykernel.zmqshell.ZMQInteractiveShell'>",
    ]
    try:
        return str(type(get_ipython())) in __VALID_NOTEBOOKS
    except NameError:
        return False