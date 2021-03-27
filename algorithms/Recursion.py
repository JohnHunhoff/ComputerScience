def factorial(i):
    """
    This return n * (n-1) *...* 1
    @param i: int
    @return: int
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    >>> factorial(3)
    6
    >>> factorial(-3)
    "don't have a result for negative numbers"
    """
    if i <= 1:
        if i < 0:
            return "don't have a result for negative numbers"
        return 1
    return i * factorial(i-1)


def sum_array(array: list) -> int:
    """
    This function calculates the sum of its elements
    @param array: list
    @return: float
    >>> sum_array([1, 2, 3])
    6
    >>> sum_array([])
    0
    >>> sum_array([-1, 2, 3])
    4
    """
    if not array:
        return 0
    return array.pop() + sum_array(array)


def length_array(array: list) -> int:
    """
    This function return the lenght of list
    @rtype: int
    @param array: list
    @return: int
    >>> length_array([])
    0
    >>> length_array([1, 2, 3])
    3
    >>> length_array([1])
    1
    """
    if not array:
        return 0
    array.remove(array[-1])  # remove the last item
    return 1 + length_array(array)


def highest_number(array: list, i: int = 0, high=False) -> list or float:
    """
    @param high: default Boolean or float
    @param i: int
    @param array: list
    @note Doctest
    >>> highest_number([])
    []
    >>> highest_number([4])
    [4]
    >>> highest_number([1, 2, 4, 3])
    4
    >>> highest_number([-3, 0, -2, -5])
    0
    """

    if i == len(array) or len(array) < 2:
        if len(array) >= 2:
            return high
        else:
            return array
    big_number = array[i] if array[i] >= high else high

    return highest_number(array, i + 1, big_number)
