su = input("Kerro sukupuolesi (M/F):")
he = int(input("Kerro hemoglobiiniarvosi (g/l):"))
if su == "M":
    print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")
    if he < 134:
         print("Hemoglobiiniarvosi on alhainen")
    elif 134 <= he <= 195:
         print("Hemoglobiiniarvosi on normaali")
    elif he > 195:
         print("Hemoglobiiniarvosi on korkea")
elif su == "F":
    print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")
    if he < 117:
         print("Hemoglobiiniarvosi on alhainen")
    elif 117 <= he <= 175:
         print("Hemoglobiiniarvosi on normaali")
    elif he > 175:
         print("Hemoglobiiniarvosi on korkea")




