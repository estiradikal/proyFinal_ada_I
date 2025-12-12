import csv

def csv_a_txt_jugadores(archivo_csv, archivo_txt):

    """Convierte un archivo CSV de jugadores a un archivo de texto con instancias de la clase Jugador.
    Suponiendo que el CSV tiene las columnas: first_name, last_name, age, puntaje.
    Ejemplo de entrada CSV: RandomData.csv
    Ejemplo de salida TXT: jugadores.txt
    """
    
    with open(archivo_csv, 'r') as f, open(archivo_txt, 'w') as out:
        rows = list(csv.DictReader(f))
        out.writelines(
            f'j{i+1} = Jugador.Jugador("{r["first_name"]} {r["last_name"]}", '
            f'{int(r["age"])}, {int(r["puntaje"])})\n'
            for i, r in enumerate(rows)
        )

def generador_equipos(archivo_salida, num_equipos, jugadores_por_equipo, num_deportes=None):
    """Genera un archivo de texto con instancias de equipos.
    
    Args:
        archivo_salida: Nombre del archivo de salida .txt
        num_equipos: Número total de equipos a generar
        jugadores_por_equipo: Jugadores por equipo
        num_deportes: Número de deportes a usar (1-10). Si None, usa todos.
    """
    
    deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Atletismo", 
                "Voleibol", "Boxeo", "Ciclismo", "Gimnasia", "Hockey"]
    
    # Limitar deportes si se especifica
    if num_deportes is not None:
        deportes = deportes[:num_deportes]
    
    with open(archivo_salida, 'w') as f:
        for i in range(num_equipos):
            deporte = deportes[i % len(deportes)]
            jug_inicial = i * jugadores_por_equipo + 1
            
            jugadores = [f"j{j}" for j in range(jug_inicial, jug_inicial + jugadores_por_equipo)]
            lista_jug = ', '.join(jugadores)
            
            f.write(f'e{i+1} = Equipo.Equipo("{deporte}", [{lista_jug}])\n')

def generar_sedes(archivo_salida, num_sedes=10, equipos_por_sede=10):

    """Genera un archivo de texto con instancias de sedes.
    Cada sede tiene un nombre de ciudad y una lista de equipos.
    Ejemplo de salida TXT: sedes.txt
    Ajustable el número de sedes y equipos por sede."""

    ciudades = ["Cali", "Medellín", "Bogotá", "Barranquilla", "Cartagena",
                "Cúcuta", "Bucaramanga", "Pereira", "Manizales", "Santa Marta"]
    
    with open(archivo_salida, 'w') as f:
        for i in range(num_sedes):
            ciudad = ciudades[i]
            equipo_inicial = i * equipos_por_sede + 1
            
            equipos = [f"e{j}" for j in range(equipo_inicial, equipo_inicial + equipos_por_sede)]
            lista_eq = ', '.join(equipos)
            
            f.write(f's{i+1} = Sede.Sede("Sede {ciudad}", [{lista_eq}])\n')

if __name__ == "__main__":
    """ Genera archivos de texto con datos de jugadores, equipos y sedes.
        Descomentar las líneas necesarias para generar los archivos deseados."""

    #csv_a_txt_jugadores('RandomData.csv', 'jugadores.txt')
    #generador_equipos('equipos.txt', num_equipos=10, jugadores_por_equipo=10, num_deportes=2)
    generar_sedes('sedes.txt', num_sedes=5, equipos_por_sede=2)

    print("Archivos generados correctamente.")
