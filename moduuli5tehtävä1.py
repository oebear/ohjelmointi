import random
kek = int(input("Anna arpakuutioiden lukumäärä:"))
p2 = []
for x in range(kek):
    p = random.randint(1, 6)
    p2.append(p)
h = sum(p2)
print(h)