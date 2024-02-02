import timeit
import random

sizes=[1000, 2000, 4000, 8000, 16000, 32000]

#follow the example in the lecture notes
def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

#follow example in the lecture notes
def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while(low <= high):
        middle = (low + high) // 2
        if (key < array[middle]):
            high = middle - 1
        elif array[middle] < key:
            low = middle + 1
        else:
            return middle
    return -1

def performance(type_of_search, array_tested, iterations):
    total = 0
    for n in range(iterations):
        key = random.choice(array_tested)
        time_analysis = timeit.timeit(lambda: type_of_search(array_tested, key), number=100)
        total += time_analysis
    average = total / 1000
    return average

#generated with chatgpt
for size in sizes:
    sorted_array = sorted(random.sample(range(1, 1000000), size))  # Sorted array for testing
    linear_avg_time = performance(linear_search, sorted_array, iterations=1000)
    binary_avg_time = performance(binary_search, sorted_array, iterations=1000)
#end of chatgpt generated code

    
