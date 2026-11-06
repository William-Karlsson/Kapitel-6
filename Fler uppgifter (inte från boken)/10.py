mening = input("Ange en mening: ")
sökord = input("Ange ett sökord: ")

ord_lista = mening.split(" ")

print(f"{sökord} förekommer {ord_lista.count(sökord)} gånger i listan.")