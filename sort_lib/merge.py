def merge(unsorted_list:list) -> list:
    """Somewhat optimized merge sort"""

    if len(unsorted_list) == 1 or (not unsorted_list):
        return unsorted_list

    length_of_list = len(unsorted_list)
    first_half = merge(unsorted_list[:length_of_list//2])
    second_half = merge(unsorted_list[length_of_list//2:])
    sorted_list = []

    while True:
        if first_half[0] > second_half[0]:
            sorted_list.append(second_half.pop(0))
            if not len(second_half):
                sorted_list.extend(first_half)
                return sorted_list
        else:
            sorted_list.append(first_half.pop(0))
            if not len(first_half):
                sorted_list.extend(second_half)
                return sorted_list


if __name__ == '__main__':
    print(merge([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))