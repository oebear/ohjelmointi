import math
def pizzahut(a,b):
    c = (a/2)**2*math.pi
    return b/c
a1 = input("Anna pizzan 1 hinta")
a2 = input("Anna pizzan 1 halkaisija")
b1 = pizzahut(int(a2),int(a1))
a1= input("Anna pizzan 2 hinta")
a2 = input("Anna pizzan 2 halkaisija")
b2 = pizzahut(int(a2),int(a1))
if b1 < b2:
    print("Pizza 1 on parempaa vastinetta rahalle")
else:
    print("Pizza 2 on parempaa vastinetta rahalle")
