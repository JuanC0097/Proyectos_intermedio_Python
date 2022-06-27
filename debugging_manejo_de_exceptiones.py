#Programa base: divisores de un n numero ingresado por el usuario
 
def divisors(num):
    divisors = []
    for i in range (1 , num +1):
        if num % i == 0:# Error esta en la divicion debe ser 0
            divisors.append(i)
    return divisors
    

#Con un bloque try and except informamos al usuario
#Si se llega a presentar una excepcion tipo ValueError
#Imprime en pantalla: Debes ingresar un numero
def run():
    try:
       num = int(input("Ingrese un numero: "))
       print(divisors(num))
       print("Finalizo el programa")
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()