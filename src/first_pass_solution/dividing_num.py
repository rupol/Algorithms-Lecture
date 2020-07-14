# We'll say that a positive int divides itself if every digit in the number divides into the number evenly
# for example, 128 divides itself since 1, 2, and 8 all divide into it evenly
# and we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself
# write a function to determine if a number divides itself
def divides_itself(num):
    # loop over each digit in num
    num_copy = num
    while num_copy >= 10:
        # get the rightmost digit of num using num % 10
        digit = num_copy % 10
        # if the digit is 0, return False
        if digit == 0:
            return False
        # take that digit and get remainder of original num / digit
        else:
            # if remainder is not 0, return False
            if num % digit != 0:
                return False
        # remove the last digit from the number using // (integer division)
        num_copy = num_copy // 10

    return True


print(divides_itself(128))  # true
print(divides_itself(121))  # false
print(divides_itself(12))  # true
print(divides_itself(120))  # false
print(divides_itself(102))  # false
