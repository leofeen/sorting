def insertion(unsorted_list:list) -> list:
    
    if (not unsorted_list) or len(unsorted_list) == 1:
        return unsorted_list


    for iteration in range(1, len(unsorted_list)):
        element = unsorted_list[iteration]
        for place in range(iteration-1, -2, -1):
            if place == -1:
                unsorted_list[0] = element
            elif element < unsorted_list[place]:
                unsorted_list[place+1] = unsorted_list[place]
            else:
                unsorted_list[place+1] = element
                break

    """for iteration in range(1, len(list_to_sort)):
        element = list_to_sort.pop(iteration)
        for place in range(iteration-1, -2, -1):
            if place == -1:
                list_to_sort[0] = element
            elif element >= list_to_sort[place]:
                list_to_sort.insert(place, element)
                break"""

    return unsorted_list


if __name__ == '__main__':
    print(insertion([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))