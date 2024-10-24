def count_digit( num):
    count = 0
    while num>0:
        num = num//10
        count +=1
    return count

print(f"digits: %d" %count_digit(3423545))