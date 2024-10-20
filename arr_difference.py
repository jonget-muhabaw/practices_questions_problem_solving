#Find the difference between two arrays (i.e., elements that are in arr1 but not in arr2)
def arr_diff(arr1, arr2):
    return list(set(arr1) - set(arr2))
    #return  [item for item in arr1 if item not in arr2]


