"""
Set - unordered, unique elements, mutable, unindexed
A set is an unordered collection of unique elements. Sets are mutable, meaning they can be modified after creation. However, sets themselves are mutable, but the elements they contain must be immutable.

syntax:

set_name = {}
set_name = set()
"""

list_ = [1,1,2,3,4,3,2,4,4]

set_nums = set(list_)
frozen_set = frozenset(set_nums)
frozen_set[1] = 11111 # TypeError: 'frozenset' object does not support item assignment
print(frozen_set)

# print(dir(frozenset))

# print(set_nums)
# 
# nums = {1,1,2,3,4,3,2,4,4}
# print(nums)

