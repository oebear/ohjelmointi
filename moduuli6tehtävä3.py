def bensa(a):
    return a*3.785
p = float(input("Miten monta gallonia?: "))
while p >= 0:
    print(f"{p}gallonia on litroina: {bensa(p)}l")
    p = float(input("Miten monta gallonia?: "))


