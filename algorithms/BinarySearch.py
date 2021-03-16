# Binary Search with list numbers.
# The max time of execution is O(log n)


def binary_search(item, ordered_list):
    """
    item = number \n
    ordered_list = Ordered integer list \n
    this function search the index of item in a 
    ordered_list with a binary search algorithm
    """

    low = 0 # low index of list
    high = len(ordered_list) - 1 # high index of list
    
    while low <= high:
        quite = (low + high) // 2
        kick = ordered_list[quite]
        
        if kick == item:
            return quite, ordered_list[quite] # return tuple(index, valor)
            
        
        elif kick > item:
            high = quite - 1

        else:
            low = quite + 1

    return None


list_of_squares = [x**2 for x in range(20)] # all perfect squares in range 0, 1, ..., 19

print(binary_search(81, list_of_squares)) # 9
