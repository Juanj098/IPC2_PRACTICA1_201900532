from nodoEncabezado import nodo_pieza
from nodo import pieza

import os

class Mtrz:
  
  def __init__(self):
    self.primero=None
    self.columnas=0
    self.filas=0
    self.contador_de_piezas=0


  def insertar_dato(self,pieza):
    if self.primero is None:
      self.primero = nodo_pieza(pieza=pieza)
      self.contador_de_piezas+=1
    else:
      actual=self.primero
      while actual.siguiente:
        actual=actual.siguiente
      actual.siguiente= nodo_pieza(pieza=pieza)
      self.contador_de_piezas+=1

  

  def recorrer_e_imprimir_lista(self):
    print("")
    print("")
    actual=self.primero
    print("**************************************************************")
    while actual!= None:
      print("Fila:",actual.pieza.fila,"Columna:",actual.pieza.columna,"Color:",actual.pieza.color)
      actual=actual.siguiente
    print("**************************************************************")
    print("")
    print("")

  def inicializar_tablero(self,filas,columnas):
    for i in range(1,filas+1):
      for j in range(1,columnas+1):
        self.insertar_dato(pieza(i,j,"w"))

  def actualizar_pieza(self,fila,columna,color):
    actual=self.primero
    while actual!=None:
      if actual.pieza.fila==fila and actual.pieza.columna==columna:
        actual.pieza.color=color
        print("Se pintó la pieza con éxito!")
        return
      actual=actual.siguiente
    print("Posición de pieza no encontrada, intente de nuevo!")
  
  def devolver_color_de_pieza(self,fila,columna):
    actual=self.primero
    while actual!=None:
      if actual.pieza.fila==fila and actual.pieza.columna==columna:
        return actual.pieza.color
      actual=actual.siguiente

  def imprimir_tablero_en_consola(self):
    for i in range(1,self.filas+1):
      for j in range(1,self.columnas+1):
        print(self.devolver_color_de_pieza(i,j),end="\t")
      print("")
    print("")

  def graficar(self,x,y):
    grp = '''digraph G {
  \trankdir=TB
  \tnode[shape=circle style=filled]
  \tNode0[label = "Colorealo"]
  '''
    nodos = ''
    col = ''
    for i in range(int(x)+1): #x -> fila
      for j in range(int(y)+1): #y -> columna
        if i != 0 and  j != 0:
          resp = self.devolver_color_de_pieza(i,j)
          if resp == 'v': #verde
            nodos  += f'\tNode{i}{j}[label="{resp}",fillcolor=green]\n'
          elif resp == 'r': #rojo
            nodos += f'\tNode{i}{j}[label="{resp}",fillcolor=red]\n'
          elif resp == 'm': #morado
            nodos += f'\tNode{i}{j}[label="{resp}",fillcolor=purple]\n'
          elif resp == 'n': #naranja
            nodos += f'\tNode{i}{j}[label="{resp}",fillcolor=orange]\n'
          elif resp == 'b': #azul
            nodos += f'\tNode{i}{j}[label="{resp}",fillcolor=blue]\n'
          elif resp =='w': #blanco
            nodos += f'\tNode{i}{j}[label="{resp}",fillcolor=white]\n'
        elif i == 0: #columnas
          nodos += f'\tNode{i}{j}[label="{j}",fillcolor=grey]\n'
          if j == 0:
            col+=f'\tNode0 -> Node{i}{j} ->'
          elif j > 0 and j < (int(y)):
            col+=f'Node{i}{j} -> ' 
          elif j == (int(y)):
            col+=f'Node{i}{j}\n'
        elif j == 0 and i > 0: #filas
          nodos += f'\tNode{i}{j}[label="{i}",fillcolor=grey]\n'

        if i > 0:
          if j == 0:
            col += f'\tNode0 -> Node{i}{j} -> '
          elif j > 0 and j < int(y):
            col += f'Node{i}{j} -> '
          elif j == int(y):
            col += f'Node{i}{j}\n'          
    grp += f'{nodos}{col}\n'
    grp += '}'
    print('Documento creado :)')
    with open('coloreando.dot','w', encoding='UTF-8') as Doc:
      Doc.write(grp)
    os.system("dot -Tpng coloreando.dot -o coloreando.png")