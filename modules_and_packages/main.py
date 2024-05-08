# from combo.a import A, A__
# from combo.b import B, B__
# from combo.c import C, C__
# 
# print(A())
# print(A__)
# print(B())
# print(B__)
# print(C())
# print(C__)

from instagram.auth import register as reg
from instagram.auth import login as lg
from instagram.post import comment as comm

print(reg.register())
print(lg.login())
print(comm.comment())