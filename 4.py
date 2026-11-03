färger = ["röd", "grön", "blå"]

nya_färger = färger.copy()

nya_färger[färger.index("grön")] = input("Vad vill du byta ut grön till?: ")

print("Här har du färgerna från början:")
for färg in färger:
    print(färg)

print("Här har du de nya färgerna:")
for färg in nya_färger:
    print(färg)

