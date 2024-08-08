import Gestion.compras as gc
import ui.uicompras as  uic
import Gestion.globales as gg


def mainmenu(op):
    title = """
    ******************
    *  Bienvenido a  *
    *     PanCamp    *
    ******************
    """

    mainmenuop = "1. Comprar 2. Vender 3. informes 4.Salir"

    gg.borrar_pantalla
    if (op !=3):
     print(title)
     print(mainmenuop)
     try:
        opcion = int(input(':)'))
     except ValueError:
        print('error en la opcion ingresada ')
        gg.pausar_pantalla()
        mainmenu(0)
     else:
        match(opcion):
           case 1:
              uic.menucompras(0)
           case 2:
               (0)
           case 3:
               (0)
           case 4:  
              print("hasta luego") 
           case _:
              print('opcion ingresada no esta en el menu de opciones')
              gg.pausar_pantalla
              mainmenu(0)

























            
