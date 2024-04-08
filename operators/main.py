"""
Operators in Python are symbols or special keywords used to perform operations on operands. Operands are the values or variables that operators act upon. Python supports various types of operators, including arithmetic operators, comparison operators, assignment operators, logical operators, bitwise operators, membership operators, and identity operators. 
"""

# arithmetic - +,-,*,/,%, //(Floor Division), **(Exponentiation)
# num1 = 2
# num2 = 4

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)
# print(num1/num2) # float
# print(num1//num2) # int
# print(num1**num2)

# assignment(shorthand) - =, +=, -=, *=, /=, %=, //=, **=

# num = 10
# num = num + 20
# num += 20
# num -= 20
# print(num)


# comparison - ==, !=, <, >, <=, >=
# num1 = 10
# num2 = 10
# num3 = 20
# 
# print(num1 == num2)
# print(num1 != num2)
# print(num1 < num3)
# print(num1 > num3)
# print(num1 <= num2)
# print(num1 >= num2)

# membership - in, not in

# name = "python"
# print('P' in name)
# print('p' in name)
# print('P' not in name)
# print('tho' not in name)
# print('Tho' not in name)

# items = ['p1', 'p2', 'p3']
# print('p1' in items)

# contact = {
#     'a': ['aman']
# }
# 
# print('b' in contact)


# identity - is, is not

# num1 = 1
# num2 = 0
# num3 = True
# num4 = False

# print(num1 is num2)
# print(num1 is not num2)

# print(num1 is num3)
# print(num1 == num3)

# num1 = 10
# num2 = '10'
# print(num1, num2)
# 
# print(id(num1))
# print(id(num2))

# Logical - and, or, not

# A B C and or
# T T T T   T
# F T T F   T
# T F T F   T
# T T F F   T
# F F F F   F

# A not
# T F
# F T

# cond1 = 1
# cond2 = 0
# cond3 = True
# cond4 = False
# cond5 = 10 < 20

# print(cond5)
# print(cond1 and cond2 and cond3) 
# print(cond3 and cond4)
# print(not cond1)
# print(cond1 or cond2)


# bitwise &, |, !, ^, <<, >>

# dec - 3
# bin - 0011

# dec - 5
# bin - 0101

# dec - 37
# bin - 100101

# 2^7 2^6 2^5 2^4 2^3 2^2 2^2 2^0
# 128 64  32  16  8   4   2   1

# A B & | ^ !
# 0 0 0 0 0 1
# 0 1 0 1 1 1
# 1 0 0 1 1 0
# 1 1 1 1 0 0
# 
# a = 3
# b = 5
# # print(a & b)
# # print(a | b)
# # print(a ^ b)
# 
# # <<, >>
# 
# x = 7 # 00000111
# x = x << 1 # 00001110 # 14
# x = x << 3 # 01110000 # 112