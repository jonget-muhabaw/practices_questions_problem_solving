import math
'''A primeproduct is a positive integer that is the product of exactly two primes greater than 1. For
example, 22 is primeproduct since 22 = 2 times 11 and both 2 and 11 are primes greater than 1.
Write a function named isPrimeProduct with an integer parameter that returns 1 if the parameter is a
primeproduct, otherwise it returns 0. Recall that a prime number is a positive integer with no factors
other than 1 and itself'''
def prime_product(num):
    product = 1
    original_num = num
    while 2*2 <=num:
           product *=2
           num //=2
    for i in range(2, int(math.sqrt(num))+1, 2):
        while num%i==0:
            product *=i
            num //=i
    if num > 2:
      product *= num     
    return True if product != original_num else None
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
        
    return True

print(prime_product(22))