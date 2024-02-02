import cProfile

def sub_function(n):
    # Sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # Third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

# Start profiling
cProfile.run('test_function()')
cProfile.run('third_function()')


'''
Answer to Questions
1. What is a profiler, and what does it do? [0.25 pts]
A profiler is used to measure a program's performance, identifying areas of code that consume the most time and resources. 
They tell programmers which functions/code are executed the most and where the program spends the most time. 
Profilers are useful for finding places in which code can be optimized. 

2. How does profiling differs from benchmarking? [0.25 pts]
Benchmarking focuses primarily on comparing the performance of different 
implementations of a program. In this sense, benchmarking is focused on the 
entire program rather than individual parts. Profiling on the otherhand 
focuses on finding performance bottlenecks in certain parts of the program. 

3. Use a profiler to measure execution time of the program (skip function
definitions) [0.25 pt]
The following is a sample output for the following program. 
         69 function calls (24 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 ex3.py:10(test_function)
    55/10    0.000    0.000    0.000    0.000 ex3.py:3(sub_function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

4. Discuss a sample output. Where does execution time go? [0.25 pts]
From the output we can see that majority of the calls are in sub_function. 
Based on the executon time we can conclude that the execution was almost immediate
and that it didn't detect any significant time being spent elsewhere. 

'''