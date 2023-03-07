try:
    x = 5/1
    x = int(input())
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("You entered something wrong")
else:
    print("else")
finally:
    print("finally")