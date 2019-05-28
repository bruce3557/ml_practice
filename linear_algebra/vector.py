import numbers

def dot_product(a, b):
    if len(a) != len(b):
        raise Exception("The length is not equal")

    result = 0
    for idx in range(len(a)):
        if not isinstance(a[idx], numbers.Number) or not isinstance(b[idx], numbers.Number):
            raise Exception("The vector is not 1D vector")
        result += a[idx] * b[idx]

    return result