tabell_övre_gräns = int(input("Hur högt vill du att din tabell ska gå till?: "))
a = []
for i in range(0,tabell_övre_gräns):
    a.append([])
    for j in range(0,tabell_övre_gräns):
        a[i].append((i+1)*(j+1))

for rad in a:
    for nummer in rad:
        print(f"{nummer:4}", end="")
    print()
