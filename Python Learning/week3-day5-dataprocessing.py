#Program 01

num_list = [2, 4, 6, 8]

double = list(map(lambda n : n*2 , num_list))
print(double)

#Program 02

num_list = [5, 12, 7, 18, 3, 20]

greater = list(filter(lambda n : n>10 , num_list))
print(greater)

#Program 03

from functools import reduce

num_list = [1, 2, 3, 4, 5]

product = reduce(lambda n1,n2 : n1 * n2 , num_list)
print(product)

#Program 04

name_list = ["ali", "umer", "sara"]

uppercase = list(map(lambda name : name.upper() ,name_list))
print(uppercase)