'''1.  Write a map function that adds plus 5 to each item in the list.'''

def map_func(lst):

    return list(map(lambda x: x + 5, lst))

print(map_func([1, 2, 3]))





'''2.  Write a map function that adds "Hello, " in front of each item in the list.'''
def map_func_2(lst):
    return list(map(lambda x: f'Hello {x}', lst))


print(map_func_2(['Ani', 'Suren', 'Nara', 'Lilit']))





'''3.  Using filter() function filter the list so that only negative numbers are left.'''
def filter_func(lst):
    return list(filter(lambda x: x > 0, lst))


print(filter_func([500, -85, 64, -9, - 478, 11]))    





'''4.  Using filter function, filter the even numbers so that only odd numbers are passed to the new list'''

def filter_func_1(lst):

    return list(filter(lambda x: x % 2 != 0, lst))


print(filter_func_1([500, -85, 64, -9, - 478, 11]))    




'''5.  Using map() and filter() functions add 2000 to the values below 8000.'''

def map_filter_func(lst):
    filtered_values = list(filter(lambda x : x < 8000, lst))
    z =  list(map(lambda x : x + 2000, filtered_values))
    return z

print(map_filter_func([5000, 7000, 9000, 6000, 10000]))





'''6.  Return product of integer lists'''
from functools import reduce

def multiply(x, y):
    return x * y

num = [5, 8, 6, 1]

result = reduce(multiply, num)

print(result)





