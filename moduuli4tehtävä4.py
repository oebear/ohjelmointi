import random
nu1 = 0
nu2 = 2
while nu1 != nu2:
    nu1 = random.randint(1, 10)
    print(nu1)
    nu2 = int(input("Arvaa nopan luku (1-10:"))
    if nu1 == nu2:
        print("Oikein")
    if nu1>nu2:
        print("Liian pieni arvaus")
    if nu1<nu2:
        print("Liian suuri arvaus")
