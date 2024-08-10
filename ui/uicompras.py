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
    gg.borrar_pantalla
    menucomprasop= '1.Pan\n2.Pasteles\n3.Bebidas\n4.Salir'
  
    if (op != 5):
       print(title)
       print(menucomprasop)
       try:
           op= int(input(":) "))
       except ValueError:
           print("opcion invalida")
           gg.pausar_pantalla
           menucomprasop(0)
    else:
           match(op):
               case 1:
                   gc.Menupanes()
               case 2:
                   ct.SearchData    
               case 3:
                   ct.ModifyData()
               case 4:
                   pass
               case 5:
                   main.mainmenu(0)
                   gg.pausar_pantalla() 
         
          
              
              
                