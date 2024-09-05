a = int(input("Anna luku:"))
for x in range(2,a):
    if a%x == 0:
        b = 1
if a%a == 0 and a%1 == 0 and b != 1:
    print("Luku on alkuluku")
elif b == 1:
    print("Luku ei ole alkuluku")