h = []
l = int(input("Anna luku:"))
h.append(int(l))
while l != "":
    l = input("Anna luku:")
    if l != "":
        h.append(int(l))
h.sort(reverse=True)
o = h[:5]
print(o)