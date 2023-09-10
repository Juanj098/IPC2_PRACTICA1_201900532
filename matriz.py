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
        self.insertar_dato(pieza(i,j,"W"))

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
