def oblicz_raty_malejace(kwota, lata, procent):
    raty = lata * 12
    rata_kapitalowa = kwota / raty
    saldo = kwota

    print("Kwota kredytu:", kwota)
    print("Liczba lat:", lata)
    print("Procent w skali roku:", procent)
    print("Typ raty: Malejące\n")
    print("Nr\tKapitał\tOdsetki\tRata\tPozostało")

    for n in range(1, raty + 1):
        odsetki = saldo * (procent / 100) / 12
        rata = rata_kapitalowa + odsetki
        print(f"{n}\t{rata_kapitalowa:.2f}\t{odsetki:.2f}\t{rata:.2f}\t{saldo - rata_kapitalowa:.2f}")
        saldo -= rata_kapitalowa

def oblicz_raty_stale(kwota, lata, procent):
    raty = lata * 12
    r = procent / 100
    q = 1 + r / 12
    rata = kwota * (q ** raty) * ((q - 1) / ((q ** raty) - 1))
    suma_odsetek = raty * rata - kwota

    print("Kwota kredytu:", kwota)
    print("Liczba lat:", lata)
    print("Procent w skali roku:", procent)
    print("Typ raty: Stałe")
    print("Całkowity koszt kredytu:", suma_odsetek + kwota)
    print("\nNr\tKapitał\tOdsetki\tRata\tPozostało")

    pozostala_kwota = kwota

    for n in range(1, raty + 1):
        odsetki = pozostala_kwota * r / 12
        kapital = rata - odsetki
        print(f"{n}\t{kapital:.2f}\t{odsetki:.2f}\t{rata:.2f}\t{pozostala_kwota - kapital:.2f}")
        pozostala_kwota -= kapital

def main():
    try:
        kwota = float(input("Kwota kredytu: "))
        lata = int(input("Liczba lat: "))
        procent = float(input("Procent w skali roku: "))
        typ = input("Typ raty (malejące/stałe): ").lower()

        if typ == "malejące":
            oblicz_raty_malejace(kwota, lata, procent)
        elif typ == "stałe":
            oblicz_raty_stale(kwota, lata, procent)
        else:
            print("Niepoprawny typ raty. Wprowadź 'malejące' lub 'stałe'.")

    except ValueError as e:
        print("Nieprawidłowa wartość:", e)
    except ZeroDivisionError:
        print("Niepoprawne dane.")

main()