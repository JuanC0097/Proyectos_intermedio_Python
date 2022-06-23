#Diccionario que albergara en sus llaves los primeros 1000
#Numero naturales y como valor guardara la raiz cuadrara de ese numero
def  run():
    my_dict = {i: i**2 for i in range(1,1001)}

    print(my_dict)
    


if __name__ == '__main__':
    run()