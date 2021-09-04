 # Python Basics Chapter 11:
# =========================
 
# 1. Introduction To *args

# to make functions flexible

# * operator
# *args

# def total(a, b):
#     return a+b

# print(total(2, 4))

# def func(*args):
#     return args

# print(func())
# print(func(2, 4, 6, "8", [10, "12"], (14, "16")))

# def total(*args):
#      return sum(args)

# print(total(1, 2, 3, 4.5, 5))

# l = [1, 2, 3, [4, 5, 6], [7, 8, 9], 10, 11]

# def ashish_que(*args):
#     total = 0
#     for arg in args:
#         for i in arg:
#             if type(i) == list:
#                 for num in i:
#                     total += num
#     return total

# print(ashish_que(l))

# args = ([1, 2, 3, [4, 5, 6], [7, 8, 9], 10, 11])

# def all_total(*args): 
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(all_total(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15))

# print(all_total(*map(int, input("Enter any numbers separated by comma : ").split(","))))

# 2. *args With Normal Parameter

# def multiply_nums(*args):
#     mul = 1
#     for arg in args:
#         mul = mul * arg
#     return mul

# print(multiply_nums())
# print(multiply_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def multiply_nums(a, *args):
#     mul = a
#     for arg in args:
#         mul *= arg
#     return mul

# print(multiply_nums(2, 2, 3))
# print(multiply_nums())
# print(multiply_nums(2))

# def multiply_nums(*args):
#     mul = 1
#     for arg in args:
#         mul *= arg
#     return mul

# print(multiply_nums())

# def multiply_nums(a, *args):
#     mul = 1
#     for arg in args:
#         mul *= arg
#     return mul

# print(multiply_num s(2))

# # 3. Args As Argument

# def multiply_nums(*args):
#     mul = 1
#     for arg in args:
#         mul *= arg
#     return mul

# print(multiply_nums(2, 3))

# nums_list = [2, 3, 4]
# nums_tuple = (2, 3, 4)

# print(multiply_nums(nums_list))
# print(multiply_nums(nums_tuple))

# # ([2, 3, 4]) -> [2, 3, 4]

# unpack elements with * operator

# print(multiply_nums(*nums_list))
# print(multiply_nums(*nums_tuple))

# 4. Exercise - 1

# Define a function -
# Input -
# num, iterable(tuple, list) containing numbers as args.

# Example -
# nums = [1, 2, 3]
# to_power(3, *nums)

# Output -
# list = [1**3, 2**3, 3**3]

# If user didn't pass any args then give a user a message 'hey you 
# didn't pass args. 

# Else return list.

# Note - Use list comprehension

# 5. Exercise - 1 Solution

# def to_power(num, *args):
#     if args:
#         return [arg**num for arg in args]
#     return 'hey you didn\'t pass args.'

# nums = [1, 2, 3]

# print(to_power(3, *nums))

# 6. Introduction To **kwargs

# kwargs => keyword arguments
# ** operator

# kwargs as a parameter

# def func(**kwargs):
#     return kwargs

# print(func(first_name='Anshul', last_name='Garg'))
# print(func())

# def func(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key} : {val}")

# func(first_name='Anshul', last_name='Garg')
# func()

# def func(name, **kwargs):
#     for key, val in kwargs.items():
#         print(f"{key} : {val}")

# func('Anshul', last_name='Garg')
# func("Anshul")
# func()

# dictionary unpacking

# def func(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key} : {val}")

# d = {'name': 'anshul', 'age' : 24}

# func(d)
# func(**d)

# # 7. Function With All Type Of Parameters

# # PADK
# # PDAK

# # parameters
# # *args
# # default parameters
# # **kwargs

# def func(first_name, *args, last_name='Garg', **kwargs):
#     print(first_name) 
#     print(args) 
#     print(last_name) 
#     print(kwargs) 

# def func(first_name, last_name='Garg', *args, **kwargs):
#     print(first_name) 
#     print(args) 
#     print(last_name) 
#     print(kwargs)

# func('Anshul', 1, 3, 5, odd1=1, odd2=3, odd3=5)
# func('Anshul', 'Kumar', 1, 3, 5, odd1=1, odd2=3, odd3=5)

# 8. Exercise - 2

# Define a function -

# names = ['anshul', 'manya']
# print(func(names))
# print(func(names, reverse_str=True))

# 9. Exercise - 2 Solution

# def func(*args, **kwargs):
#     if args:
#         if kwargs:
#             if kwargs['reverse_str'] == True:
#                 return [name[::-1] for name in args]
#             return [name for name in args]
#         return 'hey you didn\'t pass any kwargs'
#     return 'hey you didn\'t pass any args'

# names = ['anshul', 'manya']
# reverse_dict = {'reverse_str': True}

# print(func())
# print(func(*names))
# print(func(*names, reverse_str=True))
# print(func(*names, **reverse_dict))
 