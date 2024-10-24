'''Write a function that takes a list of numbers and returns a dictionary where the keys are the numbers and the values are the number of times each number appears in the list'''
def count_occurance(arr):
    element_count= {}
    for element in arr:
        if element in element_count:

            element_count[element] +=1
        else:
            element_count[element] = 1

    return element_count
'''Write a Python program to create a dictionary where the keys are numbers between 1 and 5 (both included), and the values are cubes of the keys'''
def create_dic(num):
    dic = {}
    for indx in range(1,num+1):
        dic[indx] = indx**3
    return dic

'''Write a Python program to create a dictionary where the keys are numbers between 1 and 5 (both included), and the values are cubes of the keys'''
def reverse_key_value(dic):
    reverse_dic = {}
    for key, value in dic.items():
        reverse_dic[value] = key
    return reverse_dic
'''Write a function that returns the sum of all the values in a dictionary.'''
def sum_value(dic):
    total = 0
    for key in dic:
        total += dic[key]
    return total

'''Write a Python program to create a dictionary from a list where the keys are the elements and the values are the square of the elements'''
def square_num(num):
    return {key:key*key for key in range(1,num)}
def sort_dic(dic):
    return dic.sort()