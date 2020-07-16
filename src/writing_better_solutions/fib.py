import time

import functools


@functools.lru_cache(maxsize=128)
def fib(n):
    # base case (doesn't go into recursion)
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case
    result = fib(n-1) + fib(n-2)
    return result


cache = {}


def mem_fib(n):
    # base case (doesn't go into recursion)
    if n == 0:
        cache[0] = 0
        return 0
    if n == 1:
        cache[1] = 1
        return 1
    # I want to get the answer for fib at n - 1
    # check if that value is already in the cache
    if n in cache:
        return cache[n]

    # recursive case
    result_n_1 = mem_fib(n-1)
    result_n_2 = mem_fib(n-2)
    result = result_n_1 + result_n_2
    cache[n] = result
    return result


def mem_fib_2(n, cache):
    # base case (doesn't go into recursion)
    if n == 0:
        cache[0] = 0
        return 0
    if n == 1:
        cache[1] = 1
        return 1
    # I want to get the answer for fib at n - 1
    # check if that value is already in the cache
    if n in cache:
        return cache[n]

    # recursive case
    result_n_1 = mem_fib(n-1)
    result_n_2 = mem_fib(n-2)
    result = result_n_1 + result_n_2
    cache[n] = result
    return result


def tab_fib(n):
    # start from 0 and go UP to n
    # [0, ..... 0] <- length n
    solution_table = [0 for _ in range(0, n + 1)]
    solution_table[0] = 0
    solution_table[1] = 1

    for i in range(2, n+1):
        solution_table[i] = solution_table[i-1] + solution_table[i-2]
    return solution_table[n]


start = time.time()
print(f'{fib(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n_________________________\n')

start = time.time()
print(f'{mem_fib(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n_________________________\n')

start = time.time()
print(f'{mem_fib_2(35, {})}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n_________________________\n')

start = time.time()
print(f'{tab_fib(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n_________________________\n')
