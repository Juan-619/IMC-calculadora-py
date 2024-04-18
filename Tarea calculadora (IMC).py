#Crear un programa que pida al usuario su nombre,apellido paterno y materno asi como su edad,altura y peso.
#desplegarlos con su indice de masa corporal (I.M.C)

#Le pedimos su nombre y apellidos lo guardamos en input().
nombre = input("Ingrese su nombre: ")
apellido_paterno =("Ingrese su apellido paterno: ")
apellido_materno =("Ingrese su apellido materno: ")
#Le pedimos su edad que siempre es un entero por eso el uso de int().
edad = int(input("Ingrese su edad: "))
#Pedimos su altura que es en metros y le ponenos punto por ende es un float().
altura = float(input("Ingrese su altura en metros: "))
#Pedimos su peso en (kg) pero si puede tener decimales por eso seria un float().
peso = float(input("Ingrese su peso en kilogramos: "))

#Calculo del I.M.C. peso en (kg) entre altura en (metros) elevado al cuadrado.
IMC = peso / (altura**2)

#Imprimimos el IMC
print("IMC", IMC)

#Hacemos las validaciones

if 0 <= IMC <= 15.99:
 print("Delgades severa")
elif 16.00 <= IMC <= 16.99:
 print("Delgades moderada")
elif 17.00 <= IMC <= 18.49:
 print("Delgades leve")
elif 18.50 <= IMC <= 24.99:
 print("Peso normal")
elif 25.00 <= IMC <= 29.99:
 print("Sobre peso")
elif 30.00 <= IMC <= 34.99:
 print("Obesidad leve")
elif 35.00 <= IMC <= 39.99:
 print("Obesidad media")
elif IMC >= 40.00:
 print("Obesidad mobida")
