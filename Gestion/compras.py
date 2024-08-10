import Gestion.compras as gc
import os
import modules.corefileC as mc
import Gestion.globales as gg
import main
def Menupanes(op : int):
    title ="""
    **********************************
    * Eliga el tipo de pan que desea *
    **********************************
    """
    gg.borrar_pantalla()
    Menupanesop= '1.Pan de bono\n2.Pan de Queso\n3.Pan Cascarita\n4.Pan de Yuca\n5.Calentano\n6.Rollito de sal\n7.Pan integral\n8.Pan relleno de arequipe\n9.Pan con salchicha\n10.Pan recubierto de chocolate.'
   
    if (op != 5):
       print(title)
       print(Menupanesop)