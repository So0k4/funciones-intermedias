x = [ [5,2,3], [15,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Andrés', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

def iterateDictionary(some_list):
    for directonary in some_list:
        for key, value in directonary.items():
            print(key, '-', value, end='')
        print()

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes) 
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

estudiantes = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30}
]

apellidos = [
    {'lasname': "sepulveda"},
    {'lasname': "aguirre"},
    {'lasname': "toselli"}
]

def printInfo(some_dict):
    for ubicacion in dojo['ubicaciones']:
        print(ubicacion)
        
    print("\nInstructores:")
    for instructor in dojo['instructores']:
            print(instructor)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
 