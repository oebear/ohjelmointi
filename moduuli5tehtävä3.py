a = int(input("Anna luku:"))
b = 2
for x in range(2,a):
    if a%x == 0:
        print("Luku ei ole alkuluku")
        b = 1
if b == 2:
    print("Luku on alkuluku")