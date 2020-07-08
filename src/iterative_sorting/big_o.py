# constant time O(1)
def print_num(n):
    print(n)


# still constant time, but much slower O(10000)
def print_num_10000(n):  # O(10000) * O(1) = O(10000)
    for _ in range(10000):  # O(10000)
        print(n)  # O(1)


# linear time O(n)
def print_num_n_times(n):  # O(n) * O(1) = O(n)
    for _ in range(n):  # O(n)
        print(n)  # O(1)


# still linear time, but much slower
def print_num_n_times_10000(n):  # (O(n) * O(1)) * (O(10000)) = O(n * 10000)
    for _ in range(n):  # O(n)
        print(n)  # O(1)
        for _ in range(10000):  # O(10000)
            print(n)  # O(1)


# polynomial time O(n^2)
animals = ['duck', 'chicken', 'elephant',
           'leopard', 'lion', 'beetle', 'squirrel']


def print_animal_pairs():  # O(n) * O(n) = O(n^2)
    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            print(f'{animal_1} and {animal_2}')  # O(1)


# still polynomial, but much slower
def print_animal_triplets():  # O(n) * O(n) * O(n) = O(n^3)
    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            for animal_2 in animals:  # O(n)
                print(f'{animal_1} and {animal_2}')  # O(1)


# logarithmic time O(log(n))
# the input gets reduced by a factor each iteration, much quicker!
def free_animals(animals):
    while len(animals) > 0:
        # removing half of the animals each time
        print(animals)
        animals = animals[0: len(animals) // 2]


free_animals(animals)
