#Find a duplicate elements in the given array
def find_duplicate(arr):
    new = []
    for a in arr:
        if arr.count(a) > 1 and a not in new:
            new.append(a)
    return new