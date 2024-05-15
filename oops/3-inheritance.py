# # single
# class A:
#     def a(self):
#         print("I am from class A")
# 
# class B(A):
#     def b(self):
#         print("I am from class B")
# 
# obj = B()
# # print(dir(obj))
# obj.a()
# obj.b()


# # multilevel
# class A:
#     def a(self):
#         print("I am from class A")
# 
# class B(A):
#     def b(self):
#         print("I am from class B")
# 
# class C(B):
#     def c(self):
#         print("I am from class C")
# 
# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# multiple
# class A:
#     def a(self):
#         print("I am from class A")
# 
# class B:
#     def b(self):
#         print("I am from class B")
# 
# class C(A,B):
#     def c(self):
#         print("I am from class C")
# 
# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()


# Herarchical 
# class Shape:
#     def shape(self):
#         print("from Shape class")
# 
# class Shape2d(Shape):
#     def shape2d(self):
#         print("from Shape2d class")
# 
# class Circle(Shape2d):
#     def circle(self):
#         print("from Circle class")
# 
# class Square(Shape2d):
#     def square(self):
#         print("from Square class")
# 
# class Tri(Shape2d):
#     def tri(self):
#         print("from Tri class")
# 
# 
# 
# 
# class Shape3d(Shape):
#     def shape3d(self):
#         print("from Shape3d class")
# 
# class Cube(Shape3d):
#     def cube(self):
#         print("from Cube class")
# 
# 
# obj = Square()
# # print(dir(obj))
# # print(Circle.mro())
# # print(Circle.__mro__)
# obj.square()
# obj.shape2d()
# obj.shape()
# 
# 
# 
# # obj = Cube()
# print(dir(obj))