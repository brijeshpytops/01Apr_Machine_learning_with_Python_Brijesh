# a = 10
# b = 20
# c = a + b
# print(c)
# 
# 
# x = 10
# y = 20
# z = x + y
# print(z)

# def add(a, b):
#     c = a + b
#     print(c)
# 
# add(10, 20)
# add(30, 40)

# def add(a, b):
#     return a + b
# 
# total_sum = add(40, 20)
# print(total_sum + 40)

# types of paras:

# positional para
# def add(a, b, c):
#     return a + b + c
# 
# print(add(10, 20, 30))

# default/ keyword para
# def bill(potato, tomato=20):
#     total = potato + tomato
#     print(total)
# 
# bill(30, tomato=50)

# variable length para
# *args
# **kwargs

# def add(*nums):
#     print(sum(nums))
#     print(type(nums))
# 
# add(1,2,3,4,100)

# def bill(**products):
#     # print(type(products))
#     total_amount = 0
#     for product, price in products.items():
#         print(product, price)
#         total_amount += price
#     print("Total amount : ", total_amount)
# 
# bill(pen=10, book=17.5, milk=33, chocolate=20)

# sum = lambda x:x*x*x
# print(sum(10))

# nums = [1,2,3,4,5]
# print(list(map(lambda x:x*x*x, nums)))
# print(list(map(lambda x:x*x, nums)))

# Locals and Gloabl var: 

# x = 10
# 
# def test():
#     global x
#     x = 20
#     print(x)
# 
# test()
# print(x)

# decorator

# def first_letter_cap(func):
#     def wrapper():
#         print(func().capitalize())
#         return func().capitalize()
#     return wrapper
# 
# def upper_case(func):
#     def wrapper():
#         print(func().upper())
#         return func().upper()
#     return wrapper
# 
# def count_length(func):
#     def wrapper():
#         print("Total len: ", len(func()))
#     return wrapper
# 
# @count_length
# @first_letter_cap
# @upper_case
# def test():
#     return input("Enter your name: ").lower()
# 
# test()


# def first_letter_cap(func):
#     def wrapper():
#         print(func().capitalize())
#         return func().capitalize()
#     return wrapper
# 
# def upper_case(func):
#     def wrapper():
#         print(func().upper())
#         return func().upper()
#     return wrapper
# 
# def count_length(func):
#     def wrapper():
#         result = func()
#         print("Total len: ", len(result))
#         return result
#     return wrapper
# 
# @count_length
# @first_letter_cap
# @upper_case
# def test():
#     return input("Enter your name: ").lower()
# 
# test()

# def first_letter_cap(func):
#     def wrapper():
#         result = func().capitalize()
#         print(result)
#         return result
#     return wrapper
# 
# def upper_case(func):
#     def wrapper():
#         result = func().upper()
#         print(result)
#         return result
#     return wrapper
# 
# def count_length(func):
#     def wrapper():
#         result = func()
#         print("Total len: ", len(result))
#         return result
#     return wrapper
# 
# @count_length
# @first_letter_cap
# @upper_case
# def test():
#     return input("Enter your name: ").lower()
# 
# test()

# def generator_function():
#     yield "brijesh"
#     yield "namrata"
#     yield "raj"
# 
# l  = iter(generator_function())
# # print(type(l))
# # print(l)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
