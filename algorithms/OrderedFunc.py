def search_smaller(array: list):
    """
    This function return the index of number \n
    with a linear search 
    """
    small_valor = array[0]
    small_index = 0

    for index in range(1, len(array)):
        if array[index] < small_valor:
            small_valor = array[index]
            small_index = index

    return small_index


def ordered_selection(disordered_array: list):
    """
    >>> ordered_selection([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    new_array = []
    for i in range(len(disordered_array)):
        lower_number = search_smaller(disordered_array)
        new_array.append(disordered_array.pop(lower_number))

    return new_array


print(ordered_selection([6, 7, 1, 0, -3, 6, 10]))
