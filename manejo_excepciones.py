import string

# except and try
#Se utiliza 'try' la cual ejecuta la funcion palindrome
#'except' si en dado caso al ejecutar la funcion se presenta un 
#Exception TypeError el programa imprimira un mensaje en pantalla
#def palindrome():
#    return string == string[::-1]
#try:
#    print(palindrome(1))
#except TypeError:
#    print("Solo se pueden ingresar strings")
#################################################
# 'raise' eleva un eror a una exception tipo ValueError
def palindrome():
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar un string vacio")
        return string == string[::-1]
    #Excepto si ocurre un Value error que nombraremos ve, ejecuta lo siguiente
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")


#################################################
# 'finally' se utiliza para cosas especificas como cerrar un archivo,
# cerrar una conexion con una base de datos o liberar recursos externo
#EJEMPLO
#try:
#    f = open("archivo_x.txt")
#finally:
#    f.close()


if __name__ == '__main__':
    palindrome()