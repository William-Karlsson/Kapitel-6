lista_med_tal = input("Skriv dina tal, separera dem med mellanslag: ").split(" ")

sedda_tal = set()
filterad_lista_med_tal = [tal for tal in lista_med_tal if not (tal in sedda_tal or sedda_tal.add(tal))]

print(filterad_lista_med_tal)