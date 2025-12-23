def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b 

# Preguntar al usuario la operacion que desea realizar
while True:
    try:
        operacion = float(input("Seleccione la operacion que desea realizar:""\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n"))
        if(operacion <=4 and operacion >0):
           break
    except:
        print("Por favor ingrese un numero valido.")

# Perdir al usuario los numeros a operar 
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

# Realizar la operacion seleccionada por el usuario
if operacion == 1:  
    print("El resultado de la suma es:", suma(num1, num2))
elif operacion == 2:
    print("El resultado de la resta es:", resta(num1, num2))
elif operacion == 3: 
    print("El resultado de la multiplicacion es:", multiplicacion(num1, num2))
elif operacion == 4:
    print("El resultado de la division es:", division(num1, num2))
else:
    resultado = "operacion no valida"
    print("Operacion no valida")