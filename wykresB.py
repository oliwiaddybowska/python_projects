class Wykres:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def parametry(self):
        self.a = int(input("Podaj wysokość pierwszego słupka (a): "))
        self.b = int(input("Podaj wysokość drugiego słupka (b): "))
    def warunki(self):
        try:
            if 0 <= self.a < 9 and 0 <= self.b < 9 and self.a != self.b:
                return True
            else:
                print("Wysokości słupków muszą być różne i należeć do przedziału [0, 9]. Spróbuj ponownie.")
                return False
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
            return False
    def wysokosc_trzeciego_slupka(self):
        self.c = abs(self.a - self.b)
    def wykres(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")
        print("Wykres:")
        print("--+-+--+-+--+-+--")

        wysokosc_a = "| |" if self.a >= 1 else "  "
        wysokosc_b = "| |" if self.b >= 1 else "  "
        wysokosc_c = "| |" if self.c >= 1 else "  "

        max_value = max(self.a, self.b, self.c)

        for i in range(max_value):
            line_a = "+-+" if i == self.a - 1 else f"{wysokosc_a}" if i < self.a else "  "
            line_b = "+-+" if i == self.b - 1 else f"{wysokosc_b}" if i < self.b else "  "
            line_c = "+-+" if i == self.c - 1 else f"{wysokosc_c}" if i < self.c else "  "

            print(f"  {line_a}  {line_b}  {line_c}")

if __name__ == "__main__":
    wykres = Wykres()
    wykres.parametry()

    if wykres.warunki():
        wykres.wysokosc_trzeciego_slupka()
        wykres.wykres()

