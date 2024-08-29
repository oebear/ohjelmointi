import random
print(random.randint(100,999))

while True:
    kek = str(random.randint(1000,9999))
    if kek.__contains__('0') == False and kek.__contains__('7') == False and kek.__contains__('8') == False and kek.__contains__('9') == False:
        print(kek)
        break
