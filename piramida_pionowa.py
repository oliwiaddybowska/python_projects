# wysokosc = int(input("Podaj wysokość piramidy: "))
#
# if wysokosc <= 0:
#     print("Nie można wygenerować piramidy.")
#
# y = wysokosc - 1
#
# while y >= 0:
#     x = 1
#     while x < (wysokosc * 2):
#         if x > y and x < (wysokosc * 2 - y):
#             print("#", end="")
#         else:
#             print(" ", end="")
#         x += 1
#     print("")
#     y -= 1
def generate_horizontal_pyramid(height):
    for i in range(1, height + 1):
        print("#" * i)
    for i in range(height - 1, 0, -1):
        print("#" * i)
while True:
    try:
        height: int(input("Podaj wysokość piramidy."))
    except ValueError:
        print("Wysokość piramidy musi być liczbą całkowitą.")
        continue

if height <= 0:
    print("Wysokość piramidy musi być liczbą dodatnią.")
else: generate_horizontal_pyramid()

