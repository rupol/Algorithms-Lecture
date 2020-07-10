def print_a():
    letter = "a"
    print(letter)
    # returns (implicit but can actually put it there)


def print_b():
    letter = "b"
    print(letter)


def print_c():
    letter = "c"
    print(letter)


def print_all():
    print_a()
    print_b()
    print_c()
    # only after all the above functions return will print_all return, terminating the call stack


print_all()
