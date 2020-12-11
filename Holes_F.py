# counting holes in numbers


a = input("Please enter a number: ")

if not a.isdigit():
    print("error")
    exit()
else:
    a = (a.lstrip("0"))

a = list(a)

a = [int(x) for x in a]
print(a)


def count_holes(z):
    c = 0
    for x in z:
        if x == 4 or x == 6 or x == 9 or x == 0:
            c += 1
        if x == 8:
            c += 2
    return c


x = count_holes(a)

print("number of hole: ", x)
