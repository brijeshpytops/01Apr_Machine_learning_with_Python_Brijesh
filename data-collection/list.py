"""
List - ordered, mutable, duplicate values are allowed, indexing, slicing

A list is a built-in data structure used to store a collection of items. It's one of the most versatile and commonly used data types. Lists are ordered, mutable (modifiable), and can contain elements of different data types, including numbers, strings, or even other lists.

syntax : 

list_name = []
list_name = list()

"""

products = ['i1', 'i2', 'i3', 'i4', 'i5', 'i5']

# print(type(products))
# print(len(products))

# Access 

# print(products)

# print(products[3])
# print(products[-2])

# print(products[2:])
# print(products[::-1])

# mummy = ['milk', 'butter-milk', 'tomato 1kg']
# aunty = ['gold-milk', 'tomato 1kg']
# my = ['chocolate', 'ice-cream', 'drink']
# 
# total_prodcuts = mummy + aunty + my*2
# 
# print(total_prodcuts)

items = [1, 4, 2, 3, 6, 5, 1, 4, 3]

# print(dir(items))
# 'reverse', 'sort'

# add
new_items = ['6', '7']
# items.append(new_items)
# items.extend(new_items)
# items.insert(1, new_items)

# update

# items[1] = '22' # update sepcific index value

# delete

# items.pop() # delete last value
# items.remove('3') # delete sepcific value
# del items[2] # delete sepcific index

# items.clear() # clear all elements from the list

# mix methods

# copy_list = items.copy()


# print(items.count('5'))
# print(items.index('3'))

# print(copy_list)

# items.sort(reverse=True)

# items.reverse()
# print(items)

# mix_data = [1, 2.3, 'brijesh', 2 + 3j, [11,22, [111,222, [1111,2222]]]]
# # print(mix_data)
# 
# print(mix_data[-1][-1][-1][-1])