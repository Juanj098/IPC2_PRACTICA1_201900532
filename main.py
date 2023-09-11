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
                        posx = input('Ingrese fila: ')
                        posy = input('Ingrese columna: ')
                        print('colores valido')
                        print('(v) -> Verde')
                        print('(r) -> Rojo')
                        print('(n) -> Anaranjado')
                        print('(b) -> Azul')
                        print('(m) -> Morado')
                        c = input('Ingrese color (inicial): ')
                        if c != 'v' or c != 'r' or c != 'm' or c != 'b' or c != 'n':
                            print('Color no valido')
                        os.system('cls')
                        Mtrix.actualizar_pieza(int(posx),int(posy),c)
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
        os.system('cls')
        Mtrix.graficar(x,y)
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