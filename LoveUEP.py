niu = "81933"
for i in range(1, 101):
    if i == 50:
        print(niu)
    elif i % 3 == 0 and i % 5 == 0:
        print("LoveUEP")
    elif i % 3 == 0:
        print("Love")
    elif i % 5 == 0:
        print("UEP")
    else:
        print(i)

