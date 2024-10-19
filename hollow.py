'''An array is said to be hollow if it contains 3 or more zeroes in the middle that are preceded and
followed by the same number of non-zero elements. Write a function named isHollow that accepts an
integer array and returns 1 if it is a hollow array, otherwise it returns 0'''

def isHollow(arr):
    
    i =0
    n = len(arr)
    # Step 1: Count non-zero elements before the first zero
    first_none_zero_count = 0
    while i < n and arr[i] !=0:
        i +=1
        first_none_zero_count = i
    # Step 2: Count the number of consecutive zeroes
        zero_count = 0
    while i< n and arr[i]==0:
        i +=1
        zero_count += 1

    # Step 3: Count non-zero elements after the last zero
    last_none_zero_count =  0
    while i<n and arr[i]!=0:
        i +=1
        last_none_zero_count +=1
    if zero_count >=3 and first_none_zero_count == last_none_zero_count and i==n:
        return 1
    return 0    
print(isHollow([1, 2, 0, 0, 0, 3, 4]))  
print(isHollow([1, 2, 0, 0, 3, 4]))   
print(isHollow([1, 0, 0, 0, 1]))       
print(isHollow([1, 0, 0, 0, 0, 2]))    
