# inläsning till en matris
m = []
while True:
    s = input('? ')
    if s == '':
        break
    ls = s.split(",") # Behöver bara ändre detta för att splitta på ','
    rad = [float(e) for e in ls]
    m.append(rad)