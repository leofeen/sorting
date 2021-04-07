def bubble(unsorted_list:list) -> list:
    """Basic bubble sort"""

    if (not unsorted_list) or len(unsorted_list) == 1:
        return unsorted_list
    
    list_to_sort = unsorted_list.copy()
    unsorted = True
    iteration = 1
    while unsorted:
        unsorted = False
        for i in range(0, len(list_to_sort) - iteration):
            if list_to_sort[i] > list_to_sort[i+1]:
                swap = list_to_sort[i+1]
                list_to_sort[i+1] = list_to_sort[i]
                list_to_sort[i] = swap
                unsorted = True
        iteration += 1
    return list_to_sort


if __name__ == '__main__':
    print(bubble([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))