import random
def p(a):
    b = random.randint(1, a)
    return b
b = 0
o = int(input("Anna maksimisilmäluku: "))
while b != o:
    b = p(o)
    print(b)
