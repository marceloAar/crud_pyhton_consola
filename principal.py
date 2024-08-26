import funciones 

def menu():
    print("\n===== MUNU PRINCIPAL =====")
    print("1.- Leer Productos")
    print("2.- Crear Producto")
    print("3.- Actualizar Producto")
    print("4.- Eliminar Producto")
    print("5.- Salir")
    print("=========================\n")
    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:            
            funciones.leer_productos()
            menu()
        case 2:
            print("\nCrear Nuevo Producto")            
            codigo = input("Ingrese Codigo de Producto:  ")
            nombre = input("Ingrese Nombre de Producto: ")
            precio = int(input("Ingrese Precio de Procucto $: "))
            cantidad = int(input("Ingrese Cantidad de Producto: "))
            funciones.crear_producto(codigo, nombre, precio, cantidad)
            print("Procuto ingresado...")
            menu()
        case 3:
            print("\nActualizar Producto")
            funciones.leer_productos()
            codigoActualizar = input("\nIngrese Codigo para Actualizar Producto: ")

            if funciones.actualizar_producto(codigoActualizar) == True:
                nombre = input("\nIngrese Nombre de Producto: ")
                precio = int(input("Ingrese Precio de Producto: "))
                cantidad = int(input("Ingrese Cantidad de Producto: "))
                funciones.actualizar_producto(codigoActualizar, nombre, precio, cantidad)
                print("Producto Actualizado correctamente...")
            else:
                print("Codigo de Producto no encontrado...")    

            menu()      
        case 4:
            print("opcion eliminar")
            funciones.leer_productos()            
            codigoEliminar = input("Ingrese Codigo para Eliminar Producto: ")

            if funciones.eliminar_producto(codigoEliminar) == True:
                print(f"Producto Codigo { codigoEliminar }, eliminado correctamente...")
            else:
                print("Codigo de producto no encontrado...")  

            menu()
        case 5:            
            print("Fin del programa")
        case _:
            print("Ingrese una opcion valida...")
            menu()

menu()    