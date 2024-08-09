import Gestion.compras as gc
import os
import modules.corefileC as mc
import Gestion.globales as gg
import main
def menucompras(op : int):
    title ="""
    *******************************
    *      MENU DE COMPRAS        *
    *******************************
    """
    menucomprasop= '1.Pan\n2.Pasteles\n3.Bebidas\n4. Salir'
    gg.borrar_pantalla
    if (op != 5):
       print(title)
       print(menucomprasop)
       try:
           op= int(input(": "))
       except ValueError:
           print("opcion invalida")
           gg.pausar_pantalla
           menucomprasop(0)
     
         
          
              
              
                