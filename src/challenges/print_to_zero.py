def print_to_zero(n):
    if n == 0:  # base case
        return
    print(n)
    if n < 0:
        return print_to_zero(n + 1)  # recursive case
    if n > 0:
        return print_to_zero(n - 1)  # recursive case


# print_to_zero(5)
# print_to_zero(0)
print_to_zero(-5)
