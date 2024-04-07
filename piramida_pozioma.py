wysokosc = int(input("Podaj wysokość: "))

if wysokosc <= 0:
    print("Nieprawidłowa wysokość.")

for i in range(1, wysokosc + 1):
    print("#" * i)

for i in range(wysokosc - 1, 0, -1):
    print("#" * i)


