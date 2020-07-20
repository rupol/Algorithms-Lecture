def first_func(n):
    a = 0
    while (a < n * n * n):  # O(n^3)
        a = a + n * n  # O(n^-2)
    return a


print(first_func(3))


def second_func(n):
    sum = 0
    for i in range(n):  # will run n times - O(n) * O(1) = O(n)
        j = 1  # O(1)
        while j < n:  # will run n times - O(n)
            j *= 2
            sum += 1
    return sum


print(second_func(20))
