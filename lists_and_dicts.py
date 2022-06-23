def run():
    my_list = [1,"Hello", True, 4.5]
    mu_dict = {"firstname":"juan", "lastname": "quintero"}

    super_list = [
        {"firstname":"juan", "lastname": "quintero"},
        {"firstname":"carlos", "lastname": "villar"},
        {"firstname":"adiela", "lastname": "quintero"},
        {"firstname":"fernanda", "lastname": "garcia"},
        {"firstname":"stefany", "lastname": "carvajal"},
    ]

    super_dict = {
        "natural_nums" : [5,4,9,7,3],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums" : [2.5,3.5,8.4,9.6],
    }
    #El metodo items nos permite recorrer las llaves y valores
    #al mismo tiempo de un diccionario en un ciclo
    for key, value in super_dict.items():
        print(key, "-",value)

    print('\n'.join(map(str, super_list)))

    #for x in super_list:
    #    print(x)


if __name__ == '__main__':
    run()