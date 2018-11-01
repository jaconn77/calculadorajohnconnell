

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

def salir():
    print("saliendo de calculadora")
    return exit()
while 1:
    operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide,salir): ")

    if operacion == "salir":
        print(salir())


    op1 = (float(input("Introduce el primer número: ")))

    op2 = (float(input("Introduce el segundo número: ")))


    if operacion == "suma":
        print(suma(op1, op2))

    elif operacion == "resta":
        print(resta(op1, op2))

    elif operacion == "multiplica":
        print(multiplica(op1, op2))

    elif operacion == "divide":
        if op2 != 0:
            print(divide(op1, op2))
        else:
            print("Division no es posible num2 no puede ser 0")


    else:
        print("Operación no contemplada")

    repetir = input("Operación ejecutada. Desea realizar otra operacion (si/no):   ")
    if repetir == "si":
        operacion
    else:
        salir()

