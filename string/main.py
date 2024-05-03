
# In Python, a "string" is a sequence of characters, typically used to represent text. It's one of the built-in data types in Python, and it's very versatile. Strings are immutable, meaning once they are created, their contents cannot be changed. You can create a string in Python by enclosing characters in either single quotes (''), double quotes ("") or triple quotes (""" """ or ''' '''). 

"""
"mabshjyuasg546453645@##@%$#%$     "
"""

# code = "python"
# print(len(code))
# print(type(code))

# access
# print(code)

# indexing (+/-)
# print(code[0])
# print(code[1])
# print(code[2])
# print(code[3])
# print(code[4])
# print(code[5])
# print(code[6])
# print(code[-1])
# print(code[-2])
# print(code[-6])

code = "python"

# slicing (+/-)
# print(code[start:end+1:step+1])
# print(code[2:5])
# print(code[::-1])
# print(code[::-2])

# company = "TopS TeCHnoLogY PvT. LTd."
# print(company.lower())
# print(company.upper())
# print(company.title())
# print(company.capitalize())
# print(company.swapcase())

# code = "    python is    "
# print(code.lstrip())
# print(code.rstrip())
# print(code.strip())
# print(code.replace(" ", ""))

code  = "p"
# print(code.center(20, "-"))


s = "this is a python code"
# print(s.count("is"))

# num = "657465gh"
# print(num.isnumeric())

# num = "657465gh"
# print(num.isalnum())

# num = "657465gh"
# print(not num.isalnum())


# Escap sequence
# print("\\")
# print("\'")
# print("\"")
# print("brijesh go\ndaliya")
# print("\tbrijesh")

# string formating
book = "python"
price = 23.56632
page = 400

print("Book name is python. and its price - 23.56632 and page - 400")
print(f"Book name is {book}. and its price - {price} and page - {page}")
print("Book name is {}. and its price - {} and page - {}".format(book, price, page))
print("Book name is {0}. and its price - {1} and page - {2}".format(book, price, page))
print("Book name is %s. and its price - %.5f and page - %d" % (book, price, page))
