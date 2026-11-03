lista = [__import__("random").randint(1,1000) for x in range (100)]
print(f"Minsta: {min(lista)}\nStörsta: {max(lista)}\nMedelvärde: {sum(lista)/len(lista)}")