import numpy as np
from .tensor_data import (
    count,
    index_to_position,
    broadcast_index,
    MAX_DIMS,
)
from numba import njit, prange
from .tensor import Function

count = njit()(count)
index_to_position = njit()(index_to_position)
broadcast_index = njit()(broadcast_index)


@njit(parallel=True)
def _matrix_multiply(
    out, out_shape, out_strides, a, a_shape, a_strides, b, b_shape, b_strides
):

    # TODO: Implement for Task 3.1.
    raise NotImplementedError('Need to implement for Task 3.1')
    # TODO: Implement for Task 3.1.
    raise NotImplementedError('Need to implement for Task 3.1')
