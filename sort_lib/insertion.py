def insertion(unsorted_list:list) -> list:
    
    if (not unsorted_list) or len(unsorted_list) == 1:
        return unsorted_list

    list_to_sort = unsorted_list.copy()

    for iteration in range(1, len(list_to_sort)):
        element = list_to_sort[iteration]
        for place in range(iteration-1, -2, -1):
            if place == -1:
                list_to_sort[0] = element
            elif element < list_to_sort[place]:
                list_to_sort[place+1] = list_to_sort[place]
            else:
                list_to_sort[place+1] = element
                break

    """for iteration in range(1, len(list_to_sort)):
        element = list_to_sort.pop(iteration)
        for place in range(iteration-1, -2, -1):
            if place == -1:
                list_to_sort[0] = element
            elif element >= list_to_sort[place]:
                list_to_sort.insert(place, element)
                break"""

                
    
    return list_to_sort


if __name__ == '__main__':
    print(insertion([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))