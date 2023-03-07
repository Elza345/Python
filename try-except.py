x = 0
while x == 0:
    try:
        x = int(input("Enter a number"))
        x += 5
        print(x)
    except ValueError:
        print("Enter a number")