def quick_sort(array: list) -> list:
    """
    This function return a ordered array
    @param array: disordered list
    @return: list
    @note: doctest
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    >>> quick_sort([3, -5])
    [-5, 3]
    >>> quick_sort([5, 3, 1])
    [1, 3, 5]
    >>> quick_sort([2, 3, 2, 3])
    [2, 2, 3, 3]
    >>> quick_sort([2, 3, -10, 8, 10, 5, 1.5])
    [-10, 1.5, 2, 3, 5, 8, 10]
    """
    if len(array) < 2:
        return array

    pivot = array[0]
    little_array = [i for i in array[1::] if i <= pivot]  # list of valor's little than pivot
    big_array = [i for i in array[1::] if i > pivot]  # list of valor's big than pivot

    return quick_sort(little_array) + [pivot] + quick_sort(big_array)
