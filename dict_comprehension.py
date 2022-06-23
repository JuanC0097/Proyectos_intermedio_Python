#Dictionary Comprehensions
#Diccionario de los 100 primero numeros natural
#elevados al cubo
def run():
    #Creacion de un diccionario vacio
    #my_dict = {}
    #se crea un bucle, en el que i en un rango de 1 a 100
    #En cada llave 'i' se guardara la i elevado al cubo en la llave 'i'
 
    #for i in range (1,101):
    #    my_dict[i] = i**3
    #print(my_dict)

#FORMA 1
#Guardar en las llaves del diccionario solo los numeros que no sean 
#Divicibles entre 3
    #for i in range (1,101):
    #    if i % 3 != 0:
    #        my_dict[i] = i **3
    #print(my_dict)
#FORMA CON DICTIONARY COMPREHENSIONS
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}

    print(my_dict)


if __name__ == '__main__':
    run()