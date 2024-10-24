import is_prime


def is_bunker_array(arr):
    for index,value in enumerate(arr):
        if value %2!=0 and is_prime(index+1):
            return True
        return False

print(f"At least one odd number followed by prime: {is_bunker_array([4, 9, 6, 7, 3])}")