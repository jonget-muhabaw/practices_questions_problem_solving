'''An Evens number is an integer whose digits are all even. For example 2426 is an Evens number
but 3224 is not.
Write a function named isEvens that returns 1 if its integer argument is an Evens number otherwise it
returns 0.'''

'''approache one'''
def is_even_digit(num):
    for digit in str(num):
        print("digit:%s" %digit)
        if int(digit) % 2 !=0:
            return False
    return True

'''approache two'''
def is_even(num):
    '''approch one'''
    while num > 0:
        is_even_digit = num % 10
        print("is_even_digit: %d" %is_even_digit)
        if is_even_digit % 2 != 0:
            return False
        num = num // 10
    return True
print(is_even_digit(8446))
print(is_even(8446))


