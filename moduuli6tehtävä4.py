import random
def l(a):
    return sum(a)
p = random.randint(2,9)
k = []
for a in range(1,p+1):
    k.append(random.randint(1,9))
print(l(k))
