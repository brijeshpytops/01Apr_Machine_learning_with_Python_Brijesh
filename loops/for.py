# for num in range(1, 11):
#     print(num)

# for num in range(1, 11):
#     table = 4
#     print(table, "*" , num, "=", table * num)

# print("science", "maths", "English", 'Gujrati', sep="-") # science-maths-English-Gujrati

# print("maths", end='')
# print("science", end="-")
# print("english")

# *****
# *****
# *****
# *****
# *****

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print("*", end=' ')
#     print()



# if (True):
#     print("*", end=' ')
#     print("*", end=" ")
#     print("*", end=" ")
#     print("*", end=" ")
#     print("*", end=" ")
#     
# print()
# 
# if (True):
#     print("*", end=' ')
#     print("*", end=" ")
#     print("*", end=" ")
#     print("*", end=" ")
#     print("*", end=" ")

# *
# **
# ***
# ****
# *****

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# -----
# *----
# **---
# ***--
# ****-


# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row):
#         print(" ", end=' ')
#     for col in range(num, row-1, -1):
#         print("*", end=' ')
#     print()


# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row):
#         print(" ", end=' ')
#     for col in range(num, row-1, -1):
#         print("*", end=' ')
#     for col in range(num, row, -1):
#         print("*", end=' ')
#     print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(num, row, -1):
#         print(" ", end=' ')
#     for col in range(1, row+1):
#         print("*", end=' ')
#     for col in range(1, row):
#         print("*", end=' ')
#     print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# num = 5
# for row in range(1, num+1):
#     for col in range(num, row, -1):
#         print(" ", end=' ')
#     for col in range(1, row+1):
#         print("*", end=' ')
#     for col in range(1, row):
#         print("*", end=' ')
#     print()
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end=' ')
#     for col in range(num, row, -1):
#         print("*", end=' ')
#     for col in range(num, row+1, -1):
#         print("*", end=' ')
#     print()

# *****
# *****
# *****
# *****
# *****

# num= 5
# for row in range(1, num+1):
#     print("*"*num)

# num= 5
# for row in range(1, num+1):
#     print("  "*(num-row), " * "*row)

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print(col, end=' ')
#     print()

# 65 - A 90 - Z
# 97 - a 122 - z

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print(chr(col + 64), end=' ')
#     print()
# 
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(col + 96), end=' ')
#     print()

# init = 1
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(init, end=' ')
#         init += 1
#     print()

# init = 1
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(init + 64), end=' ')
#         init += 1
#     print()
# 


# num = 5
# for row in range(1, num+1):
#     for col in range(row,0,-1):
#         print(chr(col + 64), end=' ')
#     print()




