#Constante DATA que contiene una lista de diccionarios
#todos los diccionario poseen 5 llaves que se repetiran en cada diccionario,
#un value con los datos de cada trabajador
from concurrent.futures.thread import _worker


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#Funcion que filtrara a los devs de la lista DATA que sepan el lenguaje Python

def run():
    #all_***_*** como lista que almacenara los datos de la lista DATA
    #worker nombre de los diccionarios internos
    #de worker se desea el contenido de la llave "***" 
    #con el bucle for: todos los trabajadores de la Lista data se guardara solo el contenido de la llave '***'
    #SOLO SI: la llave '******' es '****'
    #########################
    # 1 - List Comprehensions de all_python_devs
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]== "python"]

    # 1.1- High Order Futions 'filter' de all_python_devs
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))

    # 1.2- High Order Futions 'map' de all_python_devs
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    # 2 - List Comprehensions de all_platzi_devs
    all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"]== "Platzi"]

    # 2.1- High Order Futions 'filter' de  all_platzi_devs
    all_platzi_devs = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))

    # 2.2- High Order Futions 'map' =  all_platzi_devs
    all_platzi_devs = list(map(lambda worker: worker["name"], all_platzi_devs))

    # 3 - High Order Futions 'filter' de adults
    adults = list(filter(lambda worker: worker["age"]> 18, DATA))

    # 3.1 - List Comprehensions  de adults
    adults = [worker["name"] for worker in DATA if worker["age"]> 18]

    # 4 - High Order Futions 'map' de adults
    adults = list(map(lambda worker: worker["name"],adults))

    # 5 - High Order Futions 'map' de old_people
    #     Combinacion de un diccionario nuevo a nuestro diccionario actual
    #     Este diccionario contara con la llave "old" y un valor resultante
    #     De evaluar si la edad es mayor que 70 o no.
    #     Este valor se guardad en como True o False en la llave "old"
    old_people = list(map(lambda worker : worker | {"old": worker["age"] > 70}, DATA))

    # 5.1 - List Comprehensions  de old_people
    old_people = [worker |{"old": worker["age"] > 70} for worker in DATA ]
    
    #####################################################
    #se utiliza el ciclo for para imprimir la lista worker

    #1. Traer a todos los devs que manejen python
    #for worker in all_python_devs:
    #    print(worker)
    #########################################
    #2. Traer a todos los trabajadores de platzy
    #for worker in all_platzi_devs:
    #    print(worker)
    #########################################
    #3. Traer a todos los dev mayores de 18 años con la funcion filter
    #for worker in adults:
    #    print(worker)
    #########################################
    #4. Traer a todos los dev mayores de 18 años con la funcion map
    #for worker in adults:
    #    print(worker)
    #########################################
    #5. para cada uno de los trabajadores en DATA, se guardara ese diccionario
    # Sumado a un nuevo diccionario con el valor de True o False, en su caso
    #for worker in old_people:
    #    print(worker)


if __name__ == '__main__':
    run()