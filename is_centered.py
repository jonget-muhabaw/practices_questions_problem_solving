'''An array with an odd number of elements is said to be centered if all elements (except the middle
one) are strictly greater than the value of the middle element. Note that only arrays with an odd
number of elements have a middle element. Write a function named isCentered that accepts an
integer array and returns 1 if it is a centered array, otherwise it returns'''


def k_small_factors(k,num):
    for u in range(2,k):
        if num % u ==0:
            v = num//u
        if v<k:
            return True
    return False
print(k_small_factors(10,22))