import random
def pari(a):
    for e in a:
        if e%2 == 0:
            a.remove(e)
    return a
p = random.randint(5,10)
k = []
for e in range(1,p+1):
    p = random.randint(1,999)
    k.append(p)
print(k)
print(pari(k))
