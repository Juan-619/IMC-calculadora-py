#Crear un programa que pida al usuario su nombre,apellido paterno y materno asi como su edad,altura y peso.
#desplegarlos con su indice de masa corporal (I.M.C)

def calcular_IMC(peso, altura):
    """Calcula el Indice de Masa Corporal (IMC)"""
    return peso / (altura**2)

def categorizar_IMC(IMC):
    """Categoriza el IMC en base a los estandares del (ISSSTE)"""
    if IMC < 16.00:
        return "Delgadez severa"
    elif 16.00 <= IMC <= 16.99:
        return "Delgadez moderada"
    elif 17.00 <= IMC <= 18.49:
        return "Delgadez leve"
    elif 18.50 <= IMC <= 24.99:
        return "Peso normal"
    elif 25.00 <= IMC <= 29.99:
        return "Sobrepeso"
    elif 30.00 <= IMC <= 34.99:
        return "Obesidad leve"
    elif 35.00 <= IMC <= 39.99:
        return "Obesidad media"
    else:
        return "Obesidad mórbida"

def obtener_datos_personales():
    """Solicita al usuario su informacion personal"""
    print("Bienvenido al programa de cálculo del Índice de Masa Corporal (IMC)")
    nombre = input("Ingrese su nombre: ")
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")
    edad = int(input("Ingrese su edad: "))
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    return nombre, apellido_paterno, apellido_materno, edad, altura, peso

def mostrar_resultados(nombre, IMC):
    """Muestra los resultados al usuario"""
    print(f"Hola {nombre}, tu Índice de Masa Corporal (IMC) es: {IMC}")
    print("Categoría de IMC:", categorizar_IMC(IMC))

def main():
    """Funcion principal del programa"""
    nombre, apellido_paterno, apellido_materno, edad, altura, peso = obtener_datos_personales()
    IMC = calcular_IMC(peso, altura)
    mostrar_resultados(nombre, IMC)

if __name__ == "__main__":
    main()

