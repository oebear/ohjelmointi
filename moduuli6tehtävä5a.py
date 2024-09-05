def parillinen(lista):
    uusilista = []
    for each in lista:
        if each%2 == 0:
            uusilista.append(each)
    return uusilista

k = [232, 12,2,44,124]
uusilista = parillinen(k)
print(k)
print(uusilista)