import pytest

from linear_algebra import matrix

def test_transpose():
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected_result = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    test_result = matrix.transpose(input_matrix)
    assert test_result == expected_result
