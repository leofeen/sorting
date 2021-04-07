import timeit
from sort_lib.merge import merge
from sort_lib.bubble import bubble
from sort_lib.insertion import insertion

sorting_function = input('bubble, merge, insertion? ')
setup = f'from __main__ import {sorting_function}'
number = int(input('0, 1, 10 or bigger than 100 elements in list (single number): '))
if number == 0:
    print('---')
    print('Empty list:', timeit.timeit(f'{sorting_function}([])', setup))
    print('---')
elif number == 1:
    print('---')
    print('One element list:', timeit.timeit(f'{sorting_function}([1])', setup))
    print('---')
elif number == 10:
    print('---')
    print('Ten elements list:', timeit.timeit(f'{sorting_function}([45, 34, 9, 86, 33, 45, 1037, 67, 140, 2119])', setup))
    print('---')
elif number >= 100:
    import random
    number_of_iterations = int(input('How many times? '))
    setup = f'from __main__ import {sorting_function}, array'
    array = [int((random.random() * 1000) // 1) for i in range(0, number+1)]
    print('---')
    print(f'{number} elements list, {number_of_iterations} trials', timeit.timeit(f'{sorting_function}(array)', setup, number=number_of_iterations))
    #Uncomment next line to see results of sorting
    #exec(f'print({sorting_function}(array))')
    print('---')

