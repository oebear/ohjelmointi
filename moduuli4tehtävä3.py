vastr = input("Anna luku:")
vaint = int(vastr)
suurin = vaint
pienin = vaint
while vastr != "":
   if suurin < vaint:
       suurin = vaint
   if pienin > vaint:
       pienin = vaint
   vastr = input("Anna luku:")
   if vastr != "":
       vaint = int(vastr)
print(suurin)
print(pienin)