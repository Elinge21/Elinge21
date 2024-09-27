def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def Divide(n1,n2):
    return n1/n2

operation={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": Divide
}

def calculator():
    n1=int(input("Whats the first number?"))
    for symbol in operation:
        print(symbol)

    should_continue=True

    while should_continue:
        selection=input("Which operation you want to use?")

        n2=int(input("Whats the second number?"))
        calculation_function=operation[symbol]
        answer=calculation_function(n1,n2)

        print(f"{n1}{selection}{n2}={answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n'to exit:")=="y":
         n1=answer
        else:
         should_continue=False

