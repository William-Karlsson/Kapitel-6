min_lista = list(input("Vänligen ange din lista (element separerade med mellanslag): ").split(" "))
min_tuple = tuple(input("Vänligen ange din tuple: ").split(" "))

if tuple(min_lista) == min_tuple:
    print("De är lika")
else:
    print("De är inte lika")
