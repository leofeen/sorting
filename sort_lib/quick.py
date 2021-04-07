import random

def quick(unsorted_list:list) -> list:
    """Basic quick sort"""

    if (len(unsorted_list) == 1) or (not unsorted_list):
        return unsorted_list

    if len(unsorted_list) == 2:
        if unsorted_list[0] > unsorted_list[1]:
            return [unsorted_list[1], unsorted_list[0]]
        return unsorted_list

    pivot = unsorted_list.pop(random.randint(0, len(unsorted_list)-1))
    smaller_side = []
    bigger_side = []
    for item in unsorted_list:
        if item >= pivot:
            bigger_side.append(item)
        else:
            smaller_side.append(item)

    smaller_side = quick(smaller_side)
    bigger_side = quick(bigger_side)

    return smaller_side + [pivot] + bigger_side


if __name__ == '__main__':
    print(quick([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119]))