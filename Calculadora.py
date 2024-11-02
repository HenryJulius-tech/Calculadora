#henry camargo

print("Bienvenido a la calculadora")
print("Elija una operación escribiendo su nombre:")
print("suma, resta, multiplicacion, division, potencia, raiz cuadrada")

operacion = input("Ingrese la operación deseada: ").lower()

# Obtener los números necesarios
if operacion in ["suma", "resta", "multiplicacion", "division", "potencia"]:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
elif operacion == "raiz cuadrada":
    num1 = float(input("Ingrese el número: "))

# OPERACIONES A REALIZAR POR LA CALCULADORA

# Acá comienza la operación de suma - Henrry Camargo
if operacion == "suma":
    resultado = num1 + num2
    print("Resultado de la suma:", resultado)