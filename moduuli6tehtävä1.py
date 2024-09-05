import random
def noppa():
    n = random.randint(1,6)
    return n
b = 3
while b != 6:
    b = noppa()
    print(b)