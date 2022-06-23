#Lista de los primeros 100 numeros naturales elevados al cuadrado
def run():
    #Forma 1 de realizarlo
    #squares = []
    #for i in range(1,101): 
    #    squares.append(i**2)
    #print(squares)


    #FORMA 2 DE HACERLO
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    
    # Lista de los primeros 100 numeros naturales elevados al cuadrado
    # si el numero no es divisor de tres
    #squares = []
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        squares.append(i**2)
    #print(squares)
                

if __name__ == '__main__':
    run()