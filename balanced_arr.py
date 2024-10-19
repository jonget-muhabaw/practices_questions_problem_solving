'''An array is called balanced if its even numbered elements (a[0], a[2], etc.) are even and its odd
numbered elements (a[1], a[3], etc.) are odd.
Write a function named isBalanced that accepts an array of integers and returns 1 if the array is
balanced, otherwise it returns 0'''

def balanced_arr(arr):

    for index, value in enumerate(arr):
        if index % 2 ==0 and value % 2 !=0:
            return False
        if index %2 !=0 and value % 2==0:
            return False
    return True

arr = [2,3,4,7,9]
print(balanced_arr(arr))