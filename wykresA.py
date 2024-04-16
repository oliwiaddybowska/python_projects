class Wykres:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def parametry(self):
        self.a = int(input("Podaj wysokość pierwszego słupka (a): "))
        self.c = int(input("Podaj wysokość trzeciego słupka (c): "))
    def warunki(self):
        if not 0 < self.a < 20:
            print("Wysokość pierwszego słupka musi być większa od 0 i mniejsza niż 20.")
            return False
        elif not 0 < self.c < 20:
            print("Wysokość trzeciego słupka musi być większa od 0 i mniejsza niż 20.")
            return False
        elif self.a == self.c:
            print("Wysokości podanych słupków muszą być różne.")
            return False
        else:
            return True
    def wysokosc_drugiego_slupka(self):
        self.b = (int(self.a + self.c / 2))
    def wykres(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")
        print("Wykres:")
        print("+" + "-" * self.a + "+")
        print("|" + " " * self.a + "|")
        print("+" + "-" * self.a + "+")

        print("+" + "-" * self.b + "+")
        print("|" + " " * self.b + "|")
        print("+" + "-" * self.b + "+")

        print("+" + "-" * self.c + "+")
        print("|" + " " * self.c + "|")
        print("+" + "-" * self.c + "+")

if __name__ == "__main__":
    wykres = Wykres()
    wykres.parametry()

    if wykres.warunki():
        wykres.wysokosc_drugiego_slupka()
        wykres.wykres()




