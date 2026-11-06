slumpade_tal = [__import__("random").randint(1, 50) for x in range(20)]
jämna_tal = [tal for tal in slumpade_tal if tal % 2 == 0]
udda_tal = [tal for tal in slumpade_tal if tal % 2 == 1]

print("Jämn lista: ")
print(jämna_tal)
print()
print("Udda lista:")
print(udda_tal)