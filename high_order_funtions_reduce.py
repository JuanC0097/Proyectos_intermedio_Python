from functools import reduce


#Se dese reducir la lista a un unico valor
#Utilizando la funcion reduce
def  run():
    #Creacion de la lista de numeros "2", que se repite 7 veces
    numbers = [2,2,2,2,2,2,2]
    #squares: como nueva lista que guardara este valor
    #la funcion list convertira el resultado de la lambda en una lista
    #lambda recibe como parametros a y b. Como resultado multiplica a y b
    #de la lista "numbers"
    all_multiplied = reduce(lambda a,b: a * b, numbers)
    print(all_multiplied)
    


if __name__ == '__main__':
    run()