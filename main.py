from Conversor.adivina_el_numero import run as adivina_el_numero_run
from Conversor.bucles import run as bucles_run
from Conversor.break_continue import run as break_continue_run
from Conversor.conversor import run as conversor_run
from Conversor.condicionales import run as condicionales_run
from Conversor.diccionarios import run as diccionarios_run
from Conversor.diccionario_picachu import run as diccionario_picachu_run
from Conversor.contador import run as contador_run
from Conversor.funciones import run as funciones_run
from Conversor.generador_contrasena import run as generador_contrasena_run
from Conversor.palindromo import run as palindromo_run
from Conversor.prueba_primalidad import run as prueba_primalidad_run
from Conversor.recorrer import run as recorrer_run




def run():
    opcion = 15
    while opcion != 14:
        mensaje_de_inicio = """
        "Bienvenidos a las opciones del conversor: "
        1 - adivina_el_numero_run
        2 - bucles_run
        3 - break_continue_run
        4 - conversor_run
        5 - condicionales_run
        6 - diccionarios_run
        7 - diccionario_picachu_run
        8 - contador_run
        9 - funciones_run
        10 - generador_contrasena_run
        11 - palindromo_run
        12 - prueba_primalidad_run
        13 - recorrer_run
        14 - salir

        Elige una opcion: """

        print(mensaje_de_inicio)
        
        opcion =float(input("ingrese su opcion"))
        
        if opcion == 1:
            adivina_el_numero_run()
        elif opcion == 2:
            bucles_run()
        elif opcion == 3:
            break_continue_run()
        elif opcion == 4:
            conversor_run()
        elif opcion == 5:
            condicionales_run()
        elif opcion == 6:
            diccionarios_run()
        elif opcion == 7:
            diccionario_picachu_run()
        elif opcion == 8:
            contador_run()
        elif opcion == 9:
            funciones_run()
        elif opcion == 10:
            generador_contrasena_run()
        elif opcion == 11:
            palindromo_run()
        elif opcion == 12:
            prueba_primalidad_run()
        elif opcion == 13:
            recorrer_run()
        else:
            print("valor incorrecto") 



if __name__ == "__main__":
    run()
