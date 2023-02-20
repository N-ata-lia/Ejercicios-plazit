def run():
    # def imprimir_mensaje():
    #     print('Mensaje especial: ')
    #     print('¡Estoy aprendiendo a usar funciones!')


    # imprimir_mensaje()
    # imprimir_mensaje()
    # imprimir_mensaje()


    # def conversacion(mensaje):
    #     print('Hola')
    #     print('Cómo estás')
    #     print(mensaje)
    #     print('Adios')


    # opcion = int(input('Elige una opción (1, 2, 3): '))
    # if opcion == 1:
    #     conversacion('Elegiste la opción 1')
    # elif opcion == 2:
    #     conversacion('Elegiste la opción 2')
    # elif opcion == 3:
    #     conversacion('Elegiste la opción 3')
    # else:
    #     print('Escribe la opción correcta')

    def suma(a:int|float, b:int|float) -> int |float:
        """
        La funcion recibe dos numeros enteros y flotantes y retomar a la suma de dos numeros.
        """
        print('Se suman dos números')
        resultado = a + b
        return resultado

    sumatoria = suma(1, 4)
    print(sumatoria)

if __name__ == "__main__":
    run()