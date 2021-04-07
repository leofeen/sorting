def bubble(unsorted_list:list) -> list:
    """Basic bubble sort"""

    if (not unsorted_list) or len(unsorted_list) == 1:
        return unsorted_list
    
    unsorted = True
    iteration = 1
    while unsorted:
        unsorted = False
        for i in range(0, len(unsorted_list) - iteration):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                unsorted = True
        iteration += 1
    return unsorted_list


if __name__ == '__main__':
    print(bubble([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))