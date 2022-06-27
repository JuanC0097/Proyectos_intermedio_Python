#Programa que devuelve los divisores de un numero ingresa por el usuario
#Forma uno 
def divisors(num):
    divisors = []
    for i in range (1 , num +1):
        if num % i == 0:# Error esta en la divicion debe ser 0
            divisors.append(i)
    return divisors
    
    #divisors = [i for i in range(1, num + 1)if num % i == 0 ]
    #return divisors


def run():
    num = int(input("Ingrese un numero: "))
    print(divisors(num))
    print("Finalizo el programa")

if __name__ == '__main__':
    run()