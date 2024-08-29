while True:
    tuuma = float(input("Anna tuuma: "))
    if tuuma >= 0:
        print(tuuma, "tuumaa on senttimetreinä", (tuuma * 2.54))
    else:
        break