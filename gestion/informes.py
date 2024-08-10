import Gestion.compras as gc
import os
import modules.corefileC as mc
import Gestion.globales as gg
import main
def Menupanes(op : int):
    title ="""
    **********************************
    *        Menu de informes        *
    **********************************
    """
    gg.borrar_pantalla()
    Menupanesop= '1.\n2.\n3.\n4.'
   
    if (op != 5):
       print(title)
       print(Menupanesop)