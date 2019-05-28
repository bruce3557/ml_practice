import numbers


def _check_equal_length(a, b):
    return len(a) == len(b)


def _check_vector_shape(a):
    for x in a:
        if not isinstance(x, numbers.Number):
            return False
    return True


def dot_product(a, b):
    if not _check_equal_length(a, b):
        raise Exception("The length is not equal")
    if not _check_vector_shape(a) or not _check_vector_shape(b):
        raise Exception("Input vectors is not a 1D vector")

    result = 0
    for idx in range(len(a)):
        result += a[idx] * b[idx]

    return result


def add(a, b):
    if not _check_equal_length(a, b):
        raise Exception("The length is not equal")
    if not _check_vector_shape(a) or not _check_vector_shape(b):
        raise Exception("Input vectors is not a 1D vector")

    result = [0] * len(a)
    for idx in range(len(a)):
        result[idx] = a[idx] + b[idx]

    return result
