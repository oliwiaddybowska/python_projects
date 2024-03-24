tekst = input("Wprowadź tekst: ")

liczba_liter = 0
liczba_interpunkcji = 0
liczba_spacji = 0
czestotliwosc_liter = {}

import string

for znak in tekst:
    if znak.isalpha():
        liczba_liter += 1
        litera = znak.lower()
        if litera in czestotliwosc_liter:
            czestotliwosc_liter[litera] += 1
        else:
            czestotliwosc_liter[litera] = 1
    elif znak in string.punctuation:
        liczba_interpunkcji += 1
    elif znak == " ":
        liczba_spacji += 1

liczba_wyrazow = len(tekst.split())

print("Liczba liter: ", liczba_liter)
print("Liczba znaków interpunkcyjnych: ", liczba_interpunkcji)
print("Liczba spacji: ", liczba_spacji)
print("Liczba wyrazów: ", liczba_wyrazow)
print("Częstotliwość użycia liter: ")

for litera, częstotliwość in czestotliwosc_liter.items():
    print(f"{litera}: {częstotliwość}")
