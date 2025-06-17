from vehiculo import Vehiculo
from basededatos import BaseDatos

def mostrar_menu(): # Menu del programa
    print("\n--- Menu de gestion de vehiculos ---")
    print("1. Registrar Vehiculo")
    print("2. Listar Vehiculo")
    print("3. Buscar Vehiculo")
    print("4. Eliminar Vehiculo")
    print("5. Actualizar Vehiculo")
    print("6. Exportar a CSV")
    print("7. Salir")

def main(): # Controla el flujo del programa
    bd = BaseDatos() # Crea una instancia de base de datos, para abrir una conexion con la BDD
    bd.conectar() # Conexion con la base de datos

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = input("Año:")
            vehiculo = Vehiculo(marca, modelo, int(anio))
            bd.insertar_vehiculo(vehiculo)
            print("Vehiculo Registrado.")

        elif opcion == "2":
            vehiculos = bd.listar_vehiculos()
            for v in vehiculos:
                print(f"ID: {v[0]}, Marca: {v[1]}, Modelo: {v[2]}, Año: {v[3]}")


        elif opcion == "3":
            id_v = int(input("ID Vehiculo: "))
            v = bd.buscar_vehiculos(id_v)
            if v:
                print(f"ID: {v[0]}, Marca: {v[1]}, Modelo: {v[2]}, Año: {v[3]}")
            else:
                print("Vehiculo no encontrado.")

        elif opcion == "4":
            id_v = int(input("ID del Vehiculo a Eliminar: "))
            bd.eliminar_vehiculo(id_v)
            print("Vehiculo Eliminado.")

        elif opcion == "5":
            id_v = int(input("ID del Vehiculo a Actualizar: "))
            marca = input("Nueva Marca: ")
            modelo = input("Nuevo Modelo: ")
            anio = input("Nuevo Año: ")
            bd.actualizar_vehiculo(id_v, marca, modelo, int(anio))
            print("Vehiculo Actualizado.")

        elif opcion == "6":
            nombre_archivo = input("Ingrese el nombre del archivo CSV (ejemplo: vehiculos.csv): ")
            bd.exportar_csv(nombre_archivo)
            print(f"Datos exportados a {nombre_archivo}")

        elif opcion == "7":
            print("Saliendo del programa.")
            bd.cerrar_conexion()
            break

        else:
            print("Opción invalida")

if __name__ == "__main__":
    main() #Llama a la funcion en bucle