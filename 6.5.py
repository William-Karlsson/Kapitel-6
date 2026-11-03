namn = []
pris = []
while True:
    s = input('namn och pris för ett kort: ')
    if s=='':
        break
    namn_pris = s.rpartition(' ')
    namn.append(namn_pris[0])
    pris.append(int(namn_pris[2]))
m = min(pris)
k = pris.index(m)
print(namn[k] + ' är billigast')
print(f'kostnad: {m:1.2f} kr/mån')
