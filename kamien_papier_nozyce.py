import random

def gra():
    wynik_uzytkownika = 0
    wynik_komputera = 0

    while True:
        wybor_uzytkownika = input("Wybierz kamień (K), papier (P) lub nożyce (N), lub wpisz 'Q' aby zakończyć grę: ").upper()
        if wybor_uzytkownika == "Q":
            break
        if wybor_uzytkownika not in ["K", "P", "N"]:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            continue

        wybor_komputera = random.choice(["K", "P", "N"])

        print("Twój wybór:", wybor_uzytkownika)
        print("Wybór komputera:", wybor_komputera)

        if wybor_uzytkownika == wybor_komputera:
            print("Remis.")
        elif (wybor_uzytkownika == "K" and wybor_komputera == "N") or \
                (wybor_uzytkownika == "P" and wybor_komputera == "K") or \
                (wybor_uzytkownika == "N" and wybor_komputera == "P"):
            print("Wygrana!")
            wynik_uzytkownika += 1
        else:
            print("Przegrana.")
            wynik_komputera += 1

        print("Wynik:")
        print("Ty:", wynik_uzytkownika)
        print("Komputer:", wynik_komputera)

gra()
