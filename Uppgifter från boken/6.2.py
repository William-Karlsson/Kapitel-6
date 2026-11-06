lista = []

while True:
    tal = input("Vänligen skriv ett tal att lägga till eller skriv 'nah' för att sluta lägga till:")

    if tal != "nah":
        try:
            tal = int(tal)
            lista.append(tal)
        except Exception as e:
            print("nämen det får du inte göra, nu har du ju följande errormeddelande: ", e)
    else:
        break

antal_mindre_än_noll = 0
for tal in lista:
    if tal < 0: 
        antal_mindre_än_noll += 1

print("Antal mindre än noll:", antal_mindre_än_noll)
