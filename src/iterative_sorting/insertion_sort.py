my_list = [8, 5, 2, 4, 1, 3]


def insertion_sort(list_to_sort):
    # the first element is already in the "sorted side" - no code required
    # for all other items, we should start comparing
    # starting at the second item, iterate until the end of the list
    for i in range(1, len(list_to_sort)):
        # the current number at the index represents the value currently being sorted
        current_num = list_to_sort[i]
        # move the current number back through the array (to the "sorted side")
        j = i
        # keep moving until: it's greater than the number before it OR we reach the start of the list
        while j > 0 and current_num < list_to_sort[j-1]:
            # shift the current value and the one to the left of it (swap)
            # overwrite the current value with the one to the left of it
            list_to_sort[j] = list_to_sort[j-1]
            # decrement the previous value index
            j -= 1
            # at this moment, j represents the new location for the current number
        # set the value at the current index to the current number
        list_to_sort[j] = current_num

    return list_to_sort


print(insertion_sort(my_list))
