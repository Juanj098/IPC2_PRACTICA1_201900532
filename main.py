import os
from matriz import Mtrz

Mtrix = Mtrz()

os.system('cls')

print('<--------------------->')
print('A.Crear Tablero        ')
print('B.Datos del estudiante ')
print('<--------------------->')
print('          (x)          ')
print('<--------------------->')
opc = input('-> ')
os.system('cls')
while opc != 'x':
    if opc == 'A':
        os.system('cls')
        print('<------------------------->')
        x = input('Ingrese no. filas: ')
        y = input('Ingrese no. columnas: ')
        print('<------------------------->')
        print('            (x)            ')
        print('<------------------------->')
        while x != 'x' or y != 'x':
            if x != '' and y != '':
                os.system('cls')
                Mtrix.inicializar_tablero(int(x),int(y))
                Mtrix.filas = int(x)
                Mtrix.columnas = int(y)
                Mtrix.imprimir_tablero_en_consola()
                resp = True
                while resp != False:
                    print('<-------------------------->')
                    print('Ingresar Dato?')
                    print('<-------------------------->')
                    opcsn = input('(s/n): ')
                    if opcsn == 's':
                        os.system('cls')
                        Mtrix.imprimir_tablero_en_consola()
                        x = input('Ingrese fila: ')
                        y = input('Ingrese columna: ')
                        c = input('Ingrese color (inicial): ')
                        os.system('cls')
                        Mtrix.actualizar_pieza(int(x),int(y),c)
                        Mtrix.imprimir_tablero_en_consola()
                    elif opcsn == 'n':
                        resp = False
                    else:
                        os.system('cls')
                        Mtrix.imprimir_tablero_en_consola()
                        continue                
            else:
                os.system('cls')
                print('ingrese dato')
            break
            print('<------------------------->')
            x = input('Ingrese no. filas: ')
            y = input('Ingrese no. columnas: ')
            print('<------------------------->')
            print('            (x)            ')
            print('<------------------------->')


        os.system('cls')
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