#Tomar los valores impares de una lista
#Utilizando la high order funtions: filter
def  run():
    #Creacion de la lista de numeros
    numbers = [1,4,5,6,3,19,37,28,21,30,32,50]
    #por medio de una lambda function recibe como parametro una x
    #y retorna el resultado de la expresion x%2 !=0 "si x divido en 2 y su resultado es distinto a cero sera impar"
    #Como segundo parametro de lambda, es el iterable numbers
    #Este resultado lo convierto en lista con la funcion list
    odd = list(filter(lambda x: x%2 !=0, numbers))
    print(odd)
    


if __name__ == '__main__':
    run()