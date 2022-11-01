result = 0

f = float(input("Enter Number: "))

while True:

    opera = input("Enter operator: +, -, *, /, to exit enter 0 : ")

    if opera == '0':
        print(f"Result is: {f}")
        break

    s = float(input("Enter Number: "))

    if opera == '+':
        result = f + s
        f = result
        f = "{:.2f}".format(f)
        print(f"Result is: {f}")

    elif opera == '-':
        result = f - s
        f = result
        f = "{:.2f}".format(f)
        print(f"Result is: {f}")

    elif opera == '*':
        result = f * s
        f = result
        f = "{:.2f}".format(f)
        print(f"Result is: {f}")

    elif opera == '/':
        result = f / s
        f = result
        f = "{:.2f}".format(f)
        print(f"Result is: {f}")

    else:
        print("Something is Wrong")
        break