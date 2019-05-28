import pytest

from linear_algebra import vector

def test_add():
    input_vec_a = [1, 2, 3]
    input_vec_b = [2, 3, 4]
    expected_result = [3, 5, 7]
    test_result = vector.add(input_vec_a, input_vec_b)
    assert expected_result == test_result


def test_dot_product():
    input_vec_a = [1, 2, 3]
    input_vec_b = [2, 3, 4]
    expected_result = 20
    test_result = vector.dot_product(input_vec_a, input_vec_b)
    assert expected_result == test_result


def test_unequal_length_dot_product():
    with pytest.raises(Exception):
        input_vec_a = [1, 2, 3]
        input_vec_b = [2, 3]
        test_result = vector.dot_product(input_vec_a, input_vec_b)


def test_not_vector_dot_product():
    with pytest.raises(Exception):
        input_vec_a = [1, 2, 3]
        input_vec_b = [2, [3]]
        test_result = vector.dot_product(input_vec_a, input_vec_b)
