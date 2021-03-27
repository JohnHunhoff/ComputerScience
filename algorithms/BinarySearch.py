# Binary Search with list numbers.
# The max time of execution is O(log n)


def binary_search(item: int, ordered_list: list):
    """
    item = number \n
    ordered_list = Ordered integer list \n
    this function search the index of item in a 
    ordered_list with a binary search algorithm

    >>> binary_search(9, [2, 3, 9, 10])
    (2, 9)
    >>> binary_search(0, [1, 2, 3, 4])
    """

    low = 0  # low index of list
    high = len(ordered_list) - 1  # high index of list

    while low <= high:
        quite = (low + high) // 2
        kick = ordered_list[quite]

        if kick == item:
            return quite, ordered_list[quite]  # return tuple(index, valor)
        elif kick > item:
            high = quite - 1
        else:
            low = quite + 1

    return None


# all perfect squares in range 0, 1, ..., 19
list_of_squares = [x ** 2 for x in range(2_000_000)]

print(binary_search(4_000_000, list_of_squares))  # 9
