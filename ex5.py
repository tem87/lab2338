import timeit
import random
from matplotlib import pyplot as plt
#plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np
from scipy.optimize import curve_fit

sizes=[1000, 2000, 4000, 8000, 16000, 32000]


#follow the example in the lecture notes and code provided on github
def linear_search(n, l):
    for i in range(len(l)):
        if l[i] == n:
            return True
    return False

#follow example in the lecture notes
def binary_search(key, n):
    low = 0
    high = len(n) - 1
    while(low <= high):
        middle = (low + high) // 2
        if (key < n[middle]):
            high = middle - 1
        elif n[middle] < key:
            low = middle + 1
        else:
            return middle
    return -1

search_type = [linear_search, binary_search]
def fit_function(x, a, b):
    return a * x + b

#generated with chatgpt
for func in search_type:
    avgtimes = []

    for listlength in sizes:
        numbers = [x for x in range(listlength)]
        stored_measured_time = []

        for i in range(1000):
            random_element = random.choice(numbers)

            if func == linear_search:
                tm = timeit.timeit(lambda: linear_search(random_element, numbers), number=100)
            elif func == binary_search:
                numbers.sort()  # Binary search requires a sorted list
                tm = timeit.timeit(lambda: binary_search(random_element, numbers), number=100)

            stored_measured_time.append(tm / 100)

        avg = sum(stored_measured_time) / len(stored_measured_time)
        avgtimes.append(avg)
        print(f"Average time for {func.__name__} on a list of length {listlength}: {avg}")

    # Fit the data with the specified function
    params, _ = curve_fit(fit_function, sizes, avgtimes)

    # Plot the data points and the fitted curve
    plt.scatter(sizes, avgtimes, label=f"{func.__name__}")
    plt.plot(sizes, fit_function(np.array(sizes), *params), label=f"Fitted {func.__name__} Curve")
    
#end of code from chatgpt

plt.legend()
plt.xlabel('List Length')
plt.ylabel('Average Time')
plt.show()
    

    
