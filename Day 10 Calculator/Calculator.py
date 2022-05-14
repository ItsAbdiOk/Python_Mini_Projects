from Logo import logo



def Cal(Contined):
    if Contined != 0:
        num1 = Contined
    else:
        num1 = float(input("What's the first number?: "))
    print("""    +: add,
    -: subtract,
    *: multiply,
    /: divide """)
    Calculaion = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    if Calculaion == "+":
        Result = num1 + num2
    elif Calculaion == "-":
        Result = num1 - num2
    elif Calculaion == "*":
        Result = num1 * num2
    elif Calculaion == "/":
        Result = num1 / num2
    print(f'{num1} {Calculaion} {num2} = {Result}')
    return Result

Results = Cal(0)
while 1 == 1:
    Continue = input("Type 'y' to continue calculating with 127.0, or type 'n' to start a new calculation:")
    if Continue == "y":
        Cal(Results)
    else:
        Cal(0)