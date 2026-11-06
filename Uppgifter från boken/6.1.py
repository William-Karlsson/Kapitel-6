antal_i_lista = int(input("Hur många nummer vill du ha i talföljden?: "))

k = 3

talföljd = [2 * k**x or 2 for x in range(antal_i_lista)]

print(talföljd)