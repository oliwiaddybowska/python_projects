niu = [8,1,9,3]
niu.sort()

print("Lista cyfr niu:", niu)

liczba = int(input("Podaj liczbę: "))
spełnione_warunki = []

for i in range(len(niu)):
    for j in range(i+1, len(niu)):
        if niu[i] + niu[j] == liczba:
            spełnione_warunki.append((niu[i], niu[j]))
            print(f"Suma {niu[i]} + {niu[j]} = {liczba}")

for i in range(len(niu)):
    for j in range(i+1, len(niu)):
        if niu[i] * niu[j] == liczba:
            spełnione_warunki.append((niu[i], niu[j]))
            print(f"Iloczyn {[i]} * {niu[j]} = {liczba}")

if spełnione_warunki:
    print("Pary liczb spełniające warunki:", spełnione_warunki)
else:
    print("Żadna para liczb nie spełnia warunków.")
