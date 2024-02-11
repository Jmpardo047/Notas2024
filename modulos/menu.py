import os
def CreateMenu()->int:
    lstOpciones = [1,2,3,4,5,6,7]
    opciones ="1. Agregar alumno\n2. buscar alumno\n3. eliminar alumno\n4. Agregar notas de alumno\n5. Ver listado de alumnos\n6. salir "
    os.system('cls')
    print(opciones)
    try:   
        n = int(input(").."))
        if (n not in lstOpciones):
            CreateMenu()
    except ValueError:
        print('dato invalido')
        os.system('pause')
        CreateMenu()
    else:
        return n
def MenuNotas()->int:
    lstOpciones = [1,2,3]
    opciones = '1. parciales\n2. quizes\n3. trabajos'
    print('Seleccione que tipo de nota desea agregar')
    print(opciones)
    try:   
        op = int(input(").."))
        if (op not in lstOpciones):
            os.system('cls')
            MenuNotas()
    except ValueError:
        print('dato invalido')
        os.system('pause')
        os.system('cls')
        MenuNotas()
    else:
        return op
    