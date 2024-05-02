import pylab
def main():
    a = float(input("Podaj wartość parametru a: "))
    b = float(input("Podaj wartość parametru b: "))
    title = input("Podaj tytuł wykresu: ")

    start = float(input("Podaj początkową wartość zakresu x: "))
    end = float(input("Podaj końcową wartość zakresu x: "))
    step = float(input("Podaj krok dla zakresu x: "))

    x = [i for i in range(int(start), int(end) + 1, int(step))]
    y = [a * i + b for i in x]

    show_grid = input("Czy wyświetlić siatkę pomocniczą? (T/N): ").upper()
    if show_grid == 'T':
        grid_value = True
    else:
        grid_value = False

    pylab.plot(x, y)
    pylab.title(title)
    pylab.grid(grid_value)
    pylab.xlabel('x')
    pylab.ylabel('f(x)')
    pylab.show()

if __name__ == "__main__":
    main()
