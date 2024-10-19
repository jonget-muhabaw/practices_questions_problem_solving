
'''An array is defined to be complete if the conditions (a), (d) and (e) below hold.
a. The array contains even numbers
b. Let min be the smallest even number in the array.
c. Let max be the largest even number in the array.
d. min does not equal max
e. All numbers between min and max are in the array'''

def is_complete_arr(arr):
    min_val = arr[0]
    max_val = arr[0]
    even_count = 0
    # Find the minimum and maximum even numbers 
    for i in arr:
        if i % 2 == 0 and i >0:
            even_count += 1
            if  i < min_val:
                min_val = i
            if  i > max_val:
                max_val = i
    if even_count < 2 or max_val == min_val:
        return False

    for j in range(min_val, max_val):
        if j not in arr:
            return False
    return True
arr = [2, 3, 4, 5, 6, 7, 8, 12]
print(is_complete_arr(arr)) 