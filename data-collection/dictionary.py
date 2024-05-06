"""
dictionary -  key-value pairs, mutable, unordered
A dictionary is a collection of key-value pairs. It is a mutable, unordered collection, meaning it can be modified after creation, and the order of elements is not preserved. Dictionaries are often used when you need to associate keys with values and quickly look up values based on their corresponding keys.

syntax:

dict_name = {
    'key1':'value1',
    'key2':'value2',
}

dict_name = dict()

"""

contacts = {
    'A':[
        {
            'aman':{
                'mobile':['43654656654', '76347574567'],
                'email':'aman@gmail.com'
            }
        },
        {
            'ajay':{
                'mobile':['43y354554', '7634754357454345'],
                'email':'ajay@gmail.com'
            }
        }
    ],
    'B':[
        {
            'bubbn':{
                'mobile':['43623423454', '763222224567'],
                'email':'bubbn@gmail.com'
            }
        },
        {
            'bunty':{
                'mobile':['477777777', '7633333354345'],
                'email':'bunty@gmail.com'
            }
        }
    ],
}

# print(contacts)
# print(contacts['B'])
# print(contacts['B'][0]['bubbn']['mobile'][0])
# print(contacts['B'][1])

# empty_dict = dict()

# print(dir(empty_dict))


# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())

# for key, value in contacts.items():
#     print(value)

# print(contacts.get('A'))

# vegs = ['tomato', 'potato', 'onion']
# price = 50
# 
# vegis = dict()
# print(vegis.fromkeys(vegs, price))

# contacts.pop('A')
# contacts.popitem()

# print(contacts)

# 'setdefault', 'update', 

# car = {
#     'name':"BMW",
#     'price':"50L",
#     'color': 'red'
# }
# 
# car.setdefault('color', 'black')
# 
# print(car)

# new_contacts = {
#     'C':[
#         {
#             'chaman':{
#                 'mobile':6523465465326,
#                 'email':['chaman@gmail.com', 'chaman1@gmail.com']
#             }
#         }
#     ],
#     'D':[
#         {
#             'dhiran':{
#                 'mobile':6523465465326,
#                 'email':['dhiran@gmail.com', 'dhiran1@gmail.com']
#             }
#         }
#     ],
# }
# contacts.update(new_contacts)
# print(contacts)



users = []

flag = True
is_fisrt = True
while(flag):
    if not is_fisrt:
        yesNo = input("You want to continue [y/n]: ")
        if yesNo.lower() != 'y':
            flag = False
            break
        else:
            flag = True
            is_fisrt = False

    username = input("Username : ")
    email = input("Email : ")
    password = input("Password: ")
    c_password = input("Confirm password: ")

    if password == c_password:
        user = {}
        user['username'] = username
        user['email'] = email
        user['password'] = password
        users.append(user)
    
    if is_fisrt:
        is_fisrt = False
    
print(users)