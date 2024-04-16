# def oblicz_raty_malejace(kwota, lata, procent):
#     raty = lata * 12
#     rata_kapitalowa = kwota / raty
#     saldo = kwota
#
#     print("Kwota kredytu:", kwota)
#     print("Liczba lat:", lata)
#     print("Procent w skali roku:", procent)
#     print("Typ raty: Malejące\n")
#     print("Nr\tKapitał\tOdsetki\tRata\tPozostało")
#
#     for n in range(1, raty + 1):
#         odsetki = saldo * (procent / 100) / 12
#         rata = rata_kapitalowa + odsetki
#         print(f"{n}\t{rata_kapitalowa:.2f}\t{odsetki:.2f}\t{rata:.2f}\t{saldo - rata_kapitalowa:.2f}")
#         saldo -= rata_kapitalowa
#
# def oblicz_raty_stale(kwota, lata, procent):
#     raty = lata * 12
#     r = procent / 100
#     q = 1 + r / 12
#     rata = kwota * (q ** raty) * ((q - 1) / ((q ** raty) - 1))
#     suma_odsetek = raty * rata - kwota
#
#     print("Kwota kredytu:", kwota)
#     print("Liczba lat:", lata)
#     print("Procent w skali roku:", procent)
#     print("Typ raty: Stałe")
#     print("Całkowity koszt kredytu:", suma_odsetek + kwota)
#     print("\nNr\tKapitał\tOdsetki\tRata\tPozostało")
#
#     pozostala_kwota = kwota
#
#     for n in range(1, raty + 1):
#         odsetki = pozostala_kwota * r / 12
#         kapital = rata - odsetki
#         print(f"{n}\t{kapital:.2f}\t{odsetki:.2f}\t{rata:.2f}\t{pozostala_kwota - kapital:.2f}")
#         pozostala_kwota -= kapital
#
# def main():
#     try:
#         kwota = float(input("Kwota kredytu: "))
#         lata = int(input("Liczba lat: "))
#         procent = float(input("Procent w skali roku: "))
#         typ = input("Typ raty (malejące/stałe): ").lower()
#
#         if typ == "malejące":
#             oblicz_raty_malejace(kwota, lata, procent)
#         elif typ == "stałe":
#             oblicz_raty_stale(kwota, lata, procent)
#         else:
#             print("Niepoprawny typ raty. Wprowadź 'malejące' lub 'stałe'.")
#
#     except ValueError as e:
#         print("Nieprawidłowa wartość:", e)
#     except ZeroDivisionError:
#         print("Niepoprawne dane.")
#
# main()

def calculate_loan_installments(loan_amount, years, annual_interest, installment_type):
    total_interest = 0
    total_paid = 0
    monthly_interest = annual_interest / 12 / 100
    total_months = years * 12

    print("\nParametry kredytu:")
    print(f"Kwota kredytu: {loan_amount}")
    print(f"Liczba lat: {years}")
    print(f"Procent w skali roku: {annual_interest}")
    print(f"Typ raty: {installment_type}")

    if installment_type == "stałe":
        monthly_installment = loan_amount * monthly_interest / (1 - (1 + monthly_interest) ** -total_months)
        q = 1 + monthly_interest
        n = total_months
        # monthly_installment_2 = loan_amount * (q ** n) ((q - 1) / ((q ** n) - 1))
        print(f"Miesięczna rata: {monthly_installment:.2f)}") # formatuje do 2 miejsc po przecinku
        for month in range(1, total_months + 1):
            interest_part = (loan_amount - total_paid) * monthly_interest
            capital_part = monthly_installment - interest_part
            total_interest += interest_part
            total_paid += capital_part
            remaining_capital = loan_amount - total_paid
            print(f"Rata {month}, "
                  f"Kapitał: {capital_part:.2f}, "
                  f"Odsetki: {interest_part:.2f}, "
                  f"Razem: {monthly_installment:.2f}, "
                  f"Pozostało: {remaining_capital:.2f}"
                  )
    elif installment_type == "malejące":
        for month in range(1, total_months + 1):
            capital_part = loan_amount / total_months
            interest_part = (loan_amount - (capital_part * (month - 1))
        print(f"\nCałkowity kredyt (kapitał): {total_paid:.2f}")
        print(f"\nKoszt (odsetki): {total_interest:.2f}")
        print(f"\nCałkowity kredyt z kosztem (kapitał + odsetki): {total_paid + total_interest:.2f}")

    while True:
        try:
            loan_amount = float(input("Podaj kwotę kredytu: "))
            if loan_amount <= 0:
                raise ValueError
        except ValueError:
            print("Kwota kredytu musi być liczbą dodatnią.")
            continue
        try:
            years = float(input("Podaj liczbę lat: "))
            if years <= 0:
                raise ValueError
        except ValueError:
            print("Liczba lat musi być liczbą dodatnią.")
            continue
        try:
            annual_interest = float(input("Podaj procent w skali roku: "))
            if annual_interest <= 0:
                raise ValueError
        except ValueError:
            print("Procent w skali roku musi być liczbą dodatnią.")
            continue
        installment_type = input("Podaj typ raty (malejące/stałe): ")
        if installment_type not in ["stałe", "malejące"]:
            print("Typ raty to 'stałe' lub 'malejące'.")
            continue
        calculate_loan_installments(loan_amount, years, annual_interest, installment_type)
        break