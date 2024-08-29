import random
n = int(input("Anna pisteiden kokonaissumma: "))
n2 = 1
n3 = 0
while n2<=n:
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if x**2+y**2<1:
        n3 += 1
    n2 += 1
pi = (4*n3)/n
print(pi)


