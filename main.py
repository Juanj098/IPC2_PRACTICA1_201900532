import os

os.system('cls')

print('<--------------------->')
print('A.Crear Tablero        ')
print('B.Datos del estudiante ')
print('<--------------------->')
print('          (x)          ')
print('<--------------------->')
opc = input('-> ')
while opc != 'x':
    if opc == 'A':
        os.system('cls')
        pass
    elif opc == 'B':
        opc_4 = ''
        while opc_4 != 'x':
            print('<----------------Datos estudiante---------------->')
            print('<  Juan Jose Gerardi Hernandez                   >')
            print('<  201900532                                     >')
            print('<  Introduccion a la Programacion 2 seccion D    >')
            print('<  Ingenieria en ciencias y sistemas             >')
            print('<  Sexto Semestre                                >')
            print('<------------------------------------------------>')
            print('<                   (x) Salir                    >')
            print('<------------------------------------------------>')
            opc_4 = input('-> ')
            os.system('cls')
    else:
        print('Opcion invalida')
    print('<--------------------->')
    print('A.Crear Tablero        ')
    print('B.Datos del estudiante ')
    print('<--------------------->')
    print('          (x)          ')
    print('<--------------------->')
    opc = input('-> ')
    os.system('cls')