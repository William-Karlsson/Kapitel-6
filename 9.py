kö = [f"Bert {x}" for x in range(1,6)]

while True:
    if len(kö) == 0:
        break

    print(f"Nu betjänas {kö[0]}", end="")
    kö.pop(0)
    input()
