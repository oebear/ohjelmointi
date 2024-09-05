h = []
h2 = int(input("Anna luku:"))
h.append(int(h2))
l = "le"
while l != "":
    l = ""
    l = input("Anna luku:")
    if l != "":
        h.append(int(l))
h.sort(reverse=True)
o = h[:5]
print(o)