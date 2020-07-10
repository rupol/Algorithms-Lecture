my_array = [5, 9, 3, 7, 2, 8, 1, 6]

# quick sort
# chose a pivot (first number in list)
# move all elements smaller than pivot to the left of pivot
# move all elements larger than pivot to the right
# repeat steps on left and right
# sort smaller arrays in the same way until the smaller arrays have only one element


# helper function
# average case run time:
# this gets called log(n) times, because n gets halved each time we divide arrays
# each level, we do O(n) things
# worst case: would get called O(n) times, so O(n^2) - because instead of halving, your pivot is the smallest/largest
def partition(numbers):  # O(n log(n))
    # this function breaks numbers into a left, pivot and right
    left = []
    pivot = numbers[0]
    right = []
    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(numbers):  # O(n log(n))
    # base case
    # what is the easiest array to sort?
    # "conquer" step
    if len(numbers) <= 1:  # O(1)
        return numbers

    # recursive case
    # "divide" step
    # figure out how to properly split our data
    left, pivot, right = partition(numbers)
    # make an array of size one with the pivot, this is now sorted
    sorted_array = quicksort(left) + [pivot] + quicksort(right)
    return sorted_array


print(quicksort(my_array))
