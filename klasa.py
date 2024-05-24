# -*- coding: utf-8 -*-
import csv

# Zadanie 1: Klasa Przedmiot
class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzacy = prowadzacy
        self.ects = ects

    def opis(self):
        return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"


# Zadanie 2: Klasa Grupa
class Grupa:
    def __init__(self):
        self.studenci = []

    def dodaj_studenta(self, student):
        self.studenci.append(student)

    def studenci_z_numerem_indeksu(self, numer_indeksu):
        return [student for student in self.studenci if student.numer_indeksu == numer_indeksu]


# Klasa Student z zadania 3
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, oceny=None):
        if oceny is None:
            oceny = []
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny


# Zadanie 3: Średnia ocen studentów
class Grupa:
    def __init__(self):
        self.studenci = []

    def dodaj_studenta(self, student):
        self.studenci.append(student)

    def studenci_z_numerem_indeksu(self, numer_indeksu):
        return [student for student in self.studenci if student.numer_indeksu == numer_indeksu]

    def srednia_ocen(self):
        wszystkie_oceny = [ocena for student in self.studenci for ocena in student.oceny]
        if wszystkie_oceny:
            return sum(wszystkie_oceny) / len(wszystkie_oceny)
        return 0

    # Zadanie 4: Eksport danych do pliku CSV
    def eksportuj_dane_do_csv(self, plik_csv):
        with open(plik_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['imie', 'nazwisko', 'numer_indeksu'])
            for student in self.studenci:
                writer.writerow([student.imie, student.nazwisko, student.numer_indeksu])

    # Zadanie 5: Studenci z określoną średnią
    def studenci_z_wysoka_srednia(self, min_srednia):
        return [student for student in self.studenci if
                student.oceny and (sum(student.oceny) / len(student.oceny) > min_srednia)]


# Zadanie 6: Klasa PlanZajec
class PlanZajec:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def przedmioty_prowadzacego(self, prowadzacy):
        return [przedmiot for przedmiot in self.przedmioty if przedmiot.prowadzacy == prowadzacy]

    # Zadanie 7: ECTS dla przedmiotów studenta
    def ects_dla_studenta(self, student):
        suma_ects = 0
        for przedmiot in self.przedmioty:
            if przedmiot.kod_przedmiotu in student.kody_przedmiotow:
                suma_ects += przedmiot.ects
        return suma_ects