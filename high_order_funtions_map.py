#Guardar el numero elevado al cuadraro de una lista
#Utilizando la funcion Map
def  run():
    #Creacion de la lista de numeros
    numbers = [1,2,3,4,5,6,7,8,9,10]
    #la funcion list envuelve todo, map envuelve nuestra funcion lambda
    #lambda recibe un parametro 'x',retornando el resultado de X al cuadrado
    #De la lista numbers. y se guardara en una nueva lista denominada squares 
    squares = list(map(lambda x:x**2,numbers))
    print(squares)
    


if __name__ == '__main__':
    run()