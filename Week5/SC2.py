naik = list(range(1, 11))
turun = list(range(10, 0, -1))

pola = []

for i in range(len(naik)):
    pola.append(naik[i])
    pola.append(turun[i])

print(' '.join(map(str, pola)))
