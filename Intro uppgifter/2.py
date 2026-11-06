namn_lista = []

# Fråga efter alla namn
for i in range (5):
    namn = input(f"Vänligen skriv namn {i+1}: ")
    namn_lista.append(namn)

# Printa alla namn
print("Här har du alla namn:")
for namn in namn_lista:
    print(namn)