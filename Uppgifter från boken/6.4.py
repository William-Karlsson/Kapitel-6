# Jag gör så att min exempel-lista alltid tar in 10 heltal
lista = [int(input(f"Vänligen ange nummer {i}/10: ")) for i in range(1,11)]

lista_utan_noll = [x for x in lista if x != 0]

print("Här har du din lista utan nollor: ")
for nummer in lista_utan_noll:
    print(nummer)