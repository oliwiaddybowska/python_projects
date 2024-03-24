def sort_desc(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def sort_asc(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

niu = [8,1,9,3]

sorted_desc = sort_desc(niu.copy())
sorted_asc = sort_asc(niu.copy())

print("Posortowana malejąco lista:", sorted_desc)
print("Posortowana rosnąco lista:", sorted_asc)

