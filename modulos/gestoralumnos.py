import os
import modulos.menu as m
from tabulate import tabulate
alumno={

}
def AddStudent(alumnos:dict):
    id = input('Ingrese el id: ')
    nombre = input('Ingrese el nombre: ')
    edad = int(input(f'Ingrese la edad de {nombre}: '))
    email = input(f'Ingrese el email de {nombre}: ')
    notas = {
        'parciales':[],
        'quizes':[],
        'trabajos':[]
    }
    alumno = {    
    'id':id,
    'nombre':nombre,
    'edad':edad,
    'email':email,
    'notas':notas
    }  
    alumnos.update({id:alumno})

def SrchStudent(alumnos:dict):
    id = input('Ingrese el id del estudiante: ')
    data = alumnos.get(id,False)
    if (type(data) == dict):
        print(data)
        os.system('pause')
    elif ((type(data)==bool) and (data == False)):
        print('ID no encontrado')
        os.system('pause')
        SrchStudent(alumnos)

def Listdata(alumnos:dict):
    info=[]
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))
    os.system('pause')

def ValidateStudent(alumnos:dict,id:str)->bool:
    return bool(alumnos.get(id,''))

def DelStudent(alumnos:dict):
    id = input('Ingrese el id del estudiante: ')
    if(ValidateStudent(alumnos,id) == True):
        alumnos.pop(id)
    else:
        print(f'El estudiante de id {id} no esta registrado')

def DelByName(alumnos:dict):
    nombre = input('Ingrese el nombre del estudiante: ')
    for key,value in alumnos.items():
        if (nombre in value['nombre']):
            alumnos.pop(key)
            break
def addGrades(alumnos:dict):
    os.system('cls')
    id = input('Ingrese el id del estudiante: ')
    if(ValidateStudent(alumnos,id) == True):
        op = m.MenuNotas()
        alumno = alumnos.get(id)
    else:
        print(f'El estudiante de id {id} no esta registrado')
        os.system('pause')
        os.system('cls')
        addGrades(alumnos)
    if (op == 1):
        add = float(input('Ingrese la nota de parcial que quiere agregar: '))
        alumno['notas']['parciales'].append(add)
    elif (op == 2):
        add = float(input('Ingrese la nota de quiz que quiere agregar: '))
        alumno['notas']['quizes'].append(add)
    elif (op == 3):
        add = float(input('Ingrese la nota de trabajo que quiere agregar: '))
        alumno['notas']['trabajos'].append(add)