'''After escaping the pirate's cave without drowning, you stumble upon a
field where it's rumored a lot of gold can be found. You even have a map that
shows where all of the biggest hauls are located!
Unfortunately, the sun is going down, so you don't have a ton of time to 
search. You decide to take one quick pass through the field. You choose 
only to move one of three ways:
-diagonally northeast
-diagonally southeast
-straight east
If you start at the northwest corner of the field, how should you move to 
maximize the gold you collect?
Can you write a function that finds the best path through a square  
field of any size?
Ex. 
                N
Input =    [[2, 4, 1],
        W   [0, 3, 2],    E
            [1, 2, 6] 
            ]
                S
Output = '27.098 can be acquired by moving
['se', 'se']'  
(based on the Gold Mine Problem at 
https://www.geeksforgeeks.org/gold-mine-problem/?ref=lbp)
'''

import random
import time
from itertools import product


def naive_scavenging(field):
    '''This solution generates all possible sequences of directions we may 
    move. Then, it sums up the values, counts how many sequences produce the 
    target sum, and calculates the odds that someone rolling `n` dice will 
    end up with a sum equal to 3 times the number of dice.
    '''
    # generate all possible permutations of 'ne', 'e' or 'se' movements
    # that get a person across the field
    all_move_combos = list(product(['se', 'e', 'ne'], repeat=len(field) - 1))
    # for each combo of moves, try to traverse, and calculate the total gold collected
    output = ''
    max_gold = 0

    for move_combo in all_move_combos:
        # start at the top left corner
        total_gold = field[0][0]
        col = 0
        row = 0
        for direction in move_combo:
            if direction == 'se':
                # try to move south
                if row > len(field) - 1:
                    break
                else:
                    row += 1

            elif direction == 'ne':
                # try to move north
                if row <= 0:
                    break
                else:
                    row -= 1
            # always move east after moving south or north
            col += 1
            total_gold += field[row][col]
        # total gold will be equal to the gold we grabbed using this move combo
        if total_gold > max_gold:
            max_gold = total_gold
            output = f'{max_gold:.3f} gold can be aquired if we move {move_combo}'
    return output


def dp_scavenging(field):
    '''This function utilizes dynamic programming to reduce the number of 
    duplicate calculations that are performed (compared to the naive 
    approach). After a coordinate is visited, we save both i) the max
    amount of gold that can be picked up from that coordinate and ii) the
    path you'd have to travel to pick up maximum gold from that point.
    Subpaths on the eastern side of the field that we visited multiple times
    in the naive approach are only visited once using dynamic programming.
    '''
    gold_cache = [[0 for _ in range(len(field))] for _ in range(len(field))]
    # start at end of field, and work our way down
    for col in range(len(field) - 1, -1, -1):
        for row in range(len(field)):
            # take all possible directions, and figure out max gold per direction
            e_gold = 0
            ne_gold = 0
            se_gold = 0

            # gold collected if we choose to go E
            if (col != len(field) - 1):
                e_gold = gold_cache[row][col+1]
            # gold collected if we choose to go NE
            if (row != 0 and col != len(field) - 1):
                ne_gold = gold_cache[row-1][col+1]
            # gold collected if we choose to go SE
            if (row != len(field) - 1 and col != len(field) - 1):
                se_gold = gold_cache[row+1][col+1]

            current_gold = field[row][col]

            # add the current gold + the BEST amount from E/NE/SE
            # save it in cache
            gold_cache[row][col] = current_gold + max(e_gold, ne_gold, se_gold)
    best_gold = gold_cache[0][0]
    return f'{best_gold:.3f} gold is the most we can get'


def print_field(field, label):
    '''Helper function to display 2D fields  
    with gold at different coordinates
    '''
    print(label)
    for row in field:
        output = ''
        for r in row:
            output += f' {r}'
        print(f'{output}\n')
    print()


# TESTS -
# Below are a series of tests that can be utilized to demonstrate the
# improvements achieved through dynamic programming. Timing is included
# to give students an idea of how poorly some approaches scale.
# However, efficiency should also be formalized using Big O notation.

small_field = []
size = 5
for _ in range(size):
    row = []
    for _ in range(size):
        row.append(round(random.random()*random.randint(1, 9), 3))
    small_field.append(row)
print_field(small_field, 'Small field')

large_field = []
size = 16
for _ in range(size):
    row = []
    for _ in range(size):
        row.append(round(random.random()*random.randint(1, 9), 3))
    large_field.append(row
                       )
# print_field(large_field, 'Large field')

# Test 1 - Naive
print('Starting test 1, naive approach...\ncrossing small field...\n')
start = time.time()
print(f'{naive_scavenging(small_field)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')

# Test 2 - Naive
# print('Starting test 2, naive approach...\ncrossing large field...\n')
# start = time.time()
# print(f'\n{naive_scavenging(large_field)}')
# print(f'\nResult calculated in {time.time()-start:.5f} seconds')
# print('\n--------------------------------\n')

# Test 3 - Dynamic Programming
print('Starting test 3, dynamic programming...\ncrossing small field...\n')
start = time.time()
print(f'\n{dp_scavenging(small_field)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')

# Test 4 - Dynamic Programming
print('Starting test 4, dynamic programming...\ncrossing large field...\n')
start = time.time()
print(f'\n{dp_scavenging(large_field)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')
