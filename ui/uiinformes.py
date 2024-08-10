import Gestion.compras as gc
import modules.corefileC as mc
import Gestion.globales as gg
import main


def menuinformes (op) :
    title = """
*******************
*  Menu informes  *
*******************

"""
    menuinformesop= '1.Ver informes \n2.\n3.\n4. Salir'
    gg.borrar_pantalla
    if (op != 5):
       print(title)
       print(menuinformesop)
       try:
           op= int(input(": "))
       except ValueError:
           print("opcion invalida")
           gg.pausar_pantalla
           menuinformesop(0)