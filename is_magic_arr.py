

import math

'''An array is defined to be a Magic array if the sum of the primes in the array is equal to the first
element of the array. If there are no primes in the array, the first element must be 0. So {21, 3, 7, 9,
11 4, 6} is a Magic array because 3, 7, 11 are the primes in the array and they sum to 21 which is the
first element of the array. {13, 4, 4, 4, 4} is also a Magic array because the sum of the primes is 13
which is also the first element. Other Magic arrays are {10, 5, 5}, {0, 6, 8, 20} and {3}. {0} is not a
Magic array because the sum of the primes is 5+5+3 = 13. Note that -5 is not a prime because prime
numbers are positive.'''
def is_magic_arr(arr):
    prime_found = False
    prime_sum = 0
    for num in arr:
        if is_prime(num):
            prime_sum +=num
            prime_found = True
    if prime_sum == arr[0] and prime_found:
        return True
    elif arr[0]==0:
        return True
    else:
        return False

def is_prime(num):
        if num < 2:
            return False
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i ==0:
                return False
        return True

arr= [13, 4, 4, 4, 4]
print(is_magic_arr(arr))