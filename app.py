import os


def separador(car, cant):
    return car * cant

# apertura archivo dataset
def leer_archivo():
    vl = []
    with open("dataset.csv", mode="rt", encoding="utf8") as arch:        
        arch.readline() 
        linea = arch.readline()
        
        while linea != "":
            linea = linea.strip()
            datos = linea.split(',')
            
            
            if len(datos) >= 4:
                
                paises = {
                    "pais": datos[0],
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3]
                }
                
                vl.append(paises)
            
            linea = arch.readline()
            
        arch.close()
        return vl

# opcion 1: agrega un pais nuevo al dataset
def agregar_pais(extracto_dataset):
    print(separador("-", 50))
    print("AGREGAR UN NUEVO PAIS")
    print(separador("-", 50))

    pais = input("Ingrese el nombre del pais: ").strip()
    continente = input("Ingrese el continente: ").strip()
    poblacion = int(input("Ingrese la población: "))
    superficie = int(input("Ingrese la superficie: "))
    

    
    nuevo_pais = {
        "pais": pais,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    extracto_dataset.append(nuevo_pais)
    
    print(separador("-", 50))
    print(f"{pais} agregado con éxito.")
    print(separador("-", 50))

#Opcion 2: actualizar pais del dataset
def actualizar_pais(extracto_dataset):
    print(separador("-", 60))
    print("ACTUALIZAR DATOS DE POBLACION Y SUPERFICIE")
    print(separador("-", 60))

    buscador = input("Ingrese el nombre del pais a actualizar: ").strip()
    resultado = None
    
    
    for pais in extracto_dataset:
        if pais["pais"] == buscador:
            resultado = pais
            break

    if resultado is None:
        print(f"'{buscador}' no se encuentra en la base de datos.")
        print(separador("-", 60)) 
        return

    print(f"\n Datos actuales para {buscador}:")
    print(f"  Poblacion: {resultado['poblacion']}")
    print(f"  Superficie: {resultado['superficie']} km cuadrado")
    print(separador("*", 60))
    
    nueva_poblacion = int(input("Ingrese la nueva población (número entero): "))
    nueva_superficie = int(input("Ingrese la nueva superficie en km cuadrado (número entero): "))
        
    resultado["poblacion"] = nueva_poblacion
    resultado["superficie"] = nueva_superficie
        
    print(separador("-", 60))
    print(f"El Pais '{buscador}' ha sido  actualizado con exito.")
    print(f"Actualizacion: Población {nueva_poblacion}, Superficie {nueva_superficie} km cuadrado.")
    print(separador("-", 60))

#opcion 3: busqueda de pais en listado        
def buscar_pais(extracto_dataset):
    print(separador("-", 60))
    print("BUSCAR PAIS POR NOMBRE")
    print(separador("-", 60))


    busqueda = input("Ingrese el nombre del pais que desea buscar: ").strip()
    
    resultado = None
    
    
    for pais in extracto_dataset:
        if pais["pais"] == busqueda:
            resultado = pais
            break 

    
    if resultado is None:
        print(f"no existe '{busqueda}' en la dataset o ha sido mal escrito.")
    else:
        # Se encontró el país, se muestran sus datos
        print(separador("*", 60))
        print(f" Pais encontrado: {resultado['pais']}")
        print(f"  Población:    {resultado['poblacion']:,} habitantes")
        print(f"  Superficie:   {resultado['superficie']:,} km cuadrado")
        print(f"  Continente:   {resultado['continente']}")

def menu():
    extracto_dataset = leer_archivo()
    
    while True:
        print(separador("=", 80))
        print("MENU DE GESTION DE DATOS DE PAISES")
        print(separador("=", 80))
        print("1. AGREGAR UN PAIS")
        print("2. ACTUALIZAR DATOS DE POBLACION Y SUPERFICIE DE UN PAIS")
        print("3. BUSCAR UN PAIS POR NOMBRE")
        print("4. FILTRAR PAISES")
        print("5. CAMBIAR ORDEN DE PAISES")
        print("6. MOSTRAR ESTADISTICAS")
        print("7. SALIR")
        print(separador("=", 80))
        opcion = int(input("Ingrese una opcion: "))
    
        match opcion:
              # ------------------------- Opción 1 (Agregar un país) -------------------------
            case 1:
                agregar_pais(extracto_dataset)

              # ------------------------- Opción 2 (Actualizar un país) -------------------------
            case 2:
                actualizar_pais(extracto_dataset)

              # ------------------------- Opción 3 (Buscar un país) -------------------------  
            case 3:
                buscar_pais(extracto_dataset)

              # ------------------------- Opción 4 (Filtrar países) -------------------------  
            case 4:
                pass  # Implementar función de filtrar países
            
              # ------------------------- Opción 5 (Cambiar orden de países) -------------------------
            case 5:
                pass  # Implementar función de cambiar orden de países
            
              # ------------------------- Opción 6 (Mostrar estadísticas) -------------------------
            case 6:
                pass  # Implementar función de mostrar estadísticas
            
              # ------------------------- Opción 7 (Salir) -------------------------
            case 7:
                print("Saliendo del programa.")
                break
            
            # ------------------------- Opción inválida -------------------------
            case _:
                print("Opción inválida. Por favor, ingrese opción del 1 al 7.")



if __name__ == "__main__":
    menu()
