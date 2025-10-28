import os


def separador(car, cant):
    return car * cant

# Funciones de ayuda

# Verifica si el archivo existe devuelve True si existe, False si no
def existe_archivo(nombre_archivo):
    return os.path.isfile(nombre_archivo)

# Verifica si el valor es un entero positivo
def es_entero_positivo(valor):
    if valor.isdigit():
        numero = int(valor)
        return numero >= 0
    else:
        return False
    
# Normalizar string: elimina espacios extras, convierte a minúsculas y luego a título
def normalizar_string(texto):
    texto_minuscula= texto.strip().lower()
    texto_normalizado= " ".join(texto_minuscula.split())
    return texto_normalizado.title()

# Compara dos strings normalizados, devuelve True si son iguales, False si no lo son
def comparar_strings(string1, string2):
    return normalizar_string(string1) == normalizar_string(string2)

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

    pais = normalizar_string(input("Ingrese el nombre del pais: "))
    continente = normalizar_string(input("Ingrese el continente: "))
    poblacion = input("Ingrese la población: ")
    superficie = input("Ingrese la superficie: ")
    
    #validar que la poblacion y superficie sean enteros positivos
    while not es_entero_positivo(poblacion):
        print("Error: La población debe ser un número entero positivo.")
        poblacion = input("Ingrese la población: ")
    
    while not es_entero_positivo(superficie):
        print("Error: La superficie debe ser un número entero positivo.")
        superficie = input("Ingrese la superficie: ")
    
    # Verificar si el país ya existe en el dataset
    for pais_existente in extracto_dataset:
        if comparar_strings(pais_existente["pais"], pais):
            print(f"El país '{pais}' ya existe en la base de datos. No se puede agregar duplicados.")
            print(separador("-", 50))
            return # Salir de la función si el país ya existe para que no lo agregue nuevamente
        
    # Verificar que todos los campos estén completos
    if not pais or not continente or not poblacion or not superficie:
        print("Error: Todos los campos son obligatorios, no puede haber ninguno vacío.")
        print(separador("-", 50))
        return
    
    nuevo_pais = {
        "pais": pais,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
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

    buscador = normalizar_string(input("Ingrese el nombre del pais a actualizar: "))
    pais_encontrado = None
    
    
    for pais in extracto_dataset:
        if pais["pais"] == buscador:
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        print(f"'{buscador}' no se encuentra en la base de datos.")
        print(separador("-", 60)) 
        return

    print(f"\n Datos actuales para {buscador}:")
    print(f"  Poblacion: {pais_encontrado['poblacion']}")
    print(f"  Superficie: {pais_encontrado['superficie']} km cuadrado")
    print(separador("*", 60))
    
    nueva_poblacion = int(input("Ingrese la nueva población (número entero): "))
    nueva_superficie = int(input("Ingrese la nueva superficie en km cuadrado (número entero): "))
        
    pais_encontrado["poblacion"] = nueva_poblacion
    pais_encontrado["superficie"] = nueva_superficie
        
    print(separador("-", 60))
    print(f"El Pais '{buscador}' ha sido  actualizado con exito.")
    print(f"Actualizacion: Población {nueva_poblacion}, Superficie {nueva_superficie} km cuadrado.")
    print(separador("-", 60))

#opcion 3: busqueda de pais en listado        
def buscar_pais(extracto_dataset):
    print(separador("-", 60))
    print("BUSCAR PAIS POR NOMBRE")
    print(separador("-", 60))

    busqueda = normalizar_string(input("Ingrese el nombre del pais que desea buscar: "))
    
    pais_encontrado = None
    
    
    for pais in extracto_dataset:
        if pais["pais"] == busqueda:
            pais_encontrado = pais
            break 

    
    if pais_encontrado is None:
        print(f"no existe '{busqueda}' en la dataset o ha sido mal escrito.")
    else:
        # Se encontró el país, se muestran sus datos
        print(separador("*", 60))
        print(f" Pais encontrado: {pais_encontrado['pais']}")
        print(f"  Población:    {pais_encontrado['poblacion']:,} habitantes")
        print(f"  Superficie:   {pais_encontrado['superficie']:,} km cuadrado")
        print(f"  Continente:   {pais_encontrado['continente']}")

def menu():
    extracto_dataset = leer_archivo()
    
    while True:
        print(separador("=", 80))
        print("MENU DE GESTIÓN DE DATOS DE PAÍSES")
        print(separador("=", 80))
        print("1. AGREGAR UN PAÍS")
        print("2. ACTUALIZAR DATOS DE POBLACIÓN Y SUPERFICIE DE UN PAÍS")
        print("3. BUSCAR UN PAÍS POR NOMBRE")
        print("4. FILTRAR PAÍSES")
        print("5. CAMBIAR ORDEN DE PAÍSES")
        print("6. MOSTRAR ESTADÍSTICAS")
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
