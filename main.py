from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Calculadora Open Source")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Suma avanzada de N números")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "0":
        break

    if opcion == "5":
        numeros = input("Ingresa los números separados por coma: ")
        lista = [float(n) for n in numeros.split(",")]
        print("Resultado:", suma_avanzada(*lista))
    else:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            try:
                print("Resultado:", dividir(a, b))
            except ValueError as e:
                print("Error:", e)
        else:
            print("Opción inválida")
