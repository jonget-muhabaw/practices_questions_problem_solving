'''Write a function named minDistance that returns the smallest distance between two factors of a
number. For example, consider 13013 = 1*7*11*13. Its factors are 1, 7, 11, 13 and 13013.
minDistance(13013) would return 2 because the smallest distance between any two factors is 2 (13 -
11 = 2). As another example, minDistance (8) would return 1 because the factors of 8 are 1, 2, 4, 8
and the smallest distance between any two factors is 1 (2 – 1 = 1).'''
from math import inf


def min_distance_btn_factors(num):
    #Get all factors of a given number
    factors =[factor for factor in range(1,num+1) if num %factor ==0]
    #initialize diff to a large value
    diff = float(inf)
    #Loop through factors of a number
    for index,value in range(len(factors)-1):
        diff_factor = abs(factors[index+1]-factors[index])
        if diff_factor < diff:
            diff = diff_factor
    return diff