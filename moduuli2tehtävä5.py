import math

leiviska = int(input("Anna leiviskät."))
naulat = int(input("Anna naulat."))
luodit =int(input("Anna luodit."))

naulat += (leiviska*20)
luodit += (naulat*32)
gramma = luodit*13.3
gramma2 = str(gramma)
print(gramma2)
if gramma >= 1000:
    kg = gramma*10**(-3)
    kg2 = str(math.trunc(kg))
    gramma2 = gramma2[len(kg2):]
    print("Massa nykymittojen mukaan:")
    print(f"{kg2} kilogrammaa ja {gramma2} grammaa.")
else:
    print("Massa nykymittojen mukaan:")
    print(f"{gramma2} grammaa.")
