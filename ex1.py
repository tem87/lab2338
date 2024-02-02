"""
1. What does this code do? [0.1 pts]

ANSWER:  This code uses recursive approach to compute the fibonacci sequence of the integer where n is the user input. If n is 0 or 1 it returns the value n itself.

2. Is this an example of a divide-and-conquer algorithm (think carefully about this one)? [0.1 pts]

ANSWER: Yes, this is an example of divide-and-conquer alogrithm because the problem of computing the fibinacci numbers at position n is divided into two parts. 
1) first at position n-1
2) Second at position n-2
Moreover, solving these parts recursively by calling the func again meets the conquer part requirements.


3. Give an expression for the time complexity of the algorithm [0.2 pts]

ANSWER: This code has exponential time complexity because it recalculates fibonacci numbers for teh same 'n' multiple times due to the repeated recursive calls.
Expression: O(2^n)

4. Implement a version of the code which uses memoization to improve
performance [0.2 pts]

Below please!


5. Give an expression for the time complexity of the optimized algorithm [0.2pts]

ANSWER: The time complexity of the optimized code is linear time complexity.
Expression: O(n)

6. Time the original code and your improved version, for all integers between 0 and 35, and plot the results (output plots must be called ex1.6.1.jpg and
ex1.6.2.jpg) [0.2 pts]

Below please!

"""
# 4.
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

# 6. for original code
import time
import matplotlib.pyplot as plt
def original_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_fibonacci(n-1) + original_fibonacci(n-2)
original_times = []
for i in range(36):
    start_time = time.time()
    original_fibonacci(i)
    end_time = time.time()
    original_times.append(end_time - start_time)

plt.figure(figsize=(10, 6))
plt.plot(range(36), original_times, label='Original Recursive', color='blue')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.1.jpg')
plt.show()

# for optimized code
import time
import matplotlib.pyplot as plt
def fibonacci_with_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci_with_memoization(n-1, memo) + fibonacci_with_memoization(n-2, memo)
        return memo[n]
memoization_times = []
for i in range(36):
    start_time = time.time()
    fibonacci_with_memoization(i)
    end_time = time.time()
    memoization_times.append(end_time - start_time)
plt.figure(figsize=(10, 6))
plt.plot(range(36), memoization_times, label='Memoization', color='orange')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.2.jpg')
plt.show()
