class person:
    # data member 
    CONST = 'Male'

    # member function
    def __init__(self, name, age, pin):
        self.n = name # public
        self.a = age # public
        self.__p = pin # private
    
    def display(self):
        print(f"Name : {self.n}")
        print(f"Age : {self.a}")
        print(f"Pin : {self.p}")

obj = person('brijesh', '28', 1111)
# print(obj.CONST)
# obj.display()
# print(obj.n)
# print(obj.__p)
print(obj._person__p) # name mengaling (obj_name._className__varName)

