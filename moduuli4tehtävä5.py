ka = "python"
sa = "rules"
ka2 = ""
sa2= ""
nu = 1
x = 1
while nu <= 5:
    ka2 = input("Anna tunnus:")
    sa2 = input("Anna salasana:")
    nu += 1
    if ka2 == ka and sa2 == sa:
        print("Tervetuloa")
        x = 2
        break

if x == 1:
    print("Pääsy evätty")