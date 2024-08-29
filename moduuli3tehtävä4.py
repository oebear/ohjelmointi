vu = int(input("Kerro vuosiluku:"))
if vu%4 == 0:
    print("Vuosi on karkausvuosi")
if vu%100 == 0:
    pass
elif vu%400 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")