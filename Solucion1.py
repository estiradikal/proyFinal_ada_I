# --------------------------
# CLASES BÁSICAS
# --------------------------
class Jugador:
    _next_id = 1
    def __init__(self, nombre, edad, rendimiento):
        self.id = Jugador._next_id
        Jugador._next_id += 1
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento
    
    def __repr__(self):
        return f"{self.id}"

class Equipo:
    def __init__(self, deporte, jugadores):
        self.deporte = deporte
        self.jugadores = jugadores  # lista de objetos Jugador
        self.promedio = self.calcular_promedio()
    
    def calcular_promedio(self):
        if not self.jugadores:
            return 0
        return sum(j.rendimiento for j in self.jugadores) / len(self.jugadores)
    
    def __repr__(self):
        return f"{self.deporte}"

class Sede:
    def __init__(self, nombre, equipos):
        self.nombre = nombre
        self.equipos = equipos  # lista de objetos Equipo
        self.promedio = self.calcular_promedio()
        self.total_jugadores = sum(len(e.jugadores) for e in equipos)
    
    def calcular_promedio(self):
        if not self.equipos:
            return 0
        return sum(e.promedio for e in self.equipos) / len(self.equipos)
    
    def __repr__(self):
        return f"{self.nombre}"

# --------------------------
# MERGE SORT MANUAL
# --------------------------
def merge_sort_jugadores(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_jugadores(arr[:mid])
    right = merge_sort_jugadores(arr[mid:])
    return merge_jugadores(left, right)

def merge_jugadores(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Orden ascendente por rendimiento
        if left[i].rendimiento < right[j].rendimiento:
            result.append(left[i])
            i += 1
        elif left[i].rendimiento > right[j].rendimiento:
            result.append(right[j])
            j += 1
        else:
            # Empate: mayor edad primero
            if left[i].edad >= right[j].edad:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_equipos(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_equipos(arr[:mid])
    right = merge_sort_equipos(arr[mid:])
    return merge_equipos(left, right)

def merge_equipos(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Orden ascendente por promedio
        if left[i].promedio < right[j].promedio:
            result.append(left[i])
            i += 1
        elif left[i].promedio > right[j].promedio:
            result.append(right[j])
            j += 1
        else:
            # Empate: más jugadores primero
            if len(left[i].jugadores) >= len(right[j].jugadores):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_sedes(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_sedes(arr[:mid])
    right = merge_sort_sedes(arr[mid:])
    return merge_sedes(left, right)

def merge_sedes(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].promedio < right[j].promedio:
            result.append(left[i])
            i += 1
        elif left[i].promedio > right[j].promedio:
            result.append(right[j])
            j += 1
        else:
            if left[i].total_jugadores >= right[j].total_jugadores:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --------------------------
# PROCESAMIENTO
# --------------------------
def procesar_solucion1(sedes):
    # 1. Ordenar jugadores dentro de cada equipo
    for sede in sedes:
        for equipo in sede.equipos:
            equipo.jugadores = merge_sort_jugadores(equipo.jugadores)
            equipo.promedio = equipo.calcular_promedio()
    
    # 2. Ordenar equipos dentro de cada sede
    for sede in sedes:
        sede.equipos = merge_sort_equipos(sede.equipos)
        sede.promedio = sede.calcular_promedio()
        sede.total_jugadores = sum(len(e.jugadores) for e in sede.equipos)
    
    # 3. Ordenar sedes
    sedes_ordenadas = merge_sort_sedes(sedes)
    
    # 4. Ranking global
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.equipos:
            todos_jugadores.extend(equipo.jugadores)
    ranking = merge_sort_jugadores(todos_jugadores)
    
    return sedes_ordenadas, ranking

# --------------------------
# ESTADÍSTICAS
# --------------------------
def calcular_estadisticas(sedes):
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.equipos:
            todos_jugadores.extend(equipo.jugadores)
    
    if not todos_jugadores:
        return {}
    
    jugador_mayor_rend = max(todos_jugadores, key=lambda j: j.rendimiento)
    jugador_menor_rend = min(todos_jugadores, key=lambda j: j.rendimiento)
    jugador_joven = min(todos_jugadores, key=lambda j: j.edad)
    jugador_veterano = max(todos_jugadores, key=lambda j: j.edad)
    
    promedio_edad = sum(j.edad for j in todos_jugadores) / len(todos_jugadores)
    promedio_rendimiento = sum(j.rendimiento for j in todos_jugadores) / len(todos_jugadores)
    
    # Equipo con mayor y menor rendimiento
    todos_equipos = [eq for sede in sedes for eq in sede.equipos]
    equipo_mayor = max(todos_equipos, key=lambda e: e.promedio)
    equipo_mayor_sede = find_equipo_sede(equipo_mayor, sedes)
    equipo_menor = min(todos_equipos, key=lambda e: e.promedio)
    equipo_menor_sede = find_equipo_sede(equipo_menor, sedes)
    
    return {
        "jugador_mayor_rend": jugador_mayor_rend,
        "jugador_menor_rend": jugador_menor_rend,
        "jugador_joven": jugador_joven,
        "jugador_veterano": jugador_veterano,
        "promedio_edad": promedio_edad,
        "promedio_rendimiento": promedio_rendimiento,
        "equipo_mayor": equipo_mayor,
        "equipo_mayor_sede": equipo_mayor_sede,
        "equipo_menor": equipo_menor,
        "equipo_menor_sede": equipo_menor_sede
    }

def find_equipo_sede(equipo, sedes):
    for sede in sedes:
        if equipo in sede.equipos:
            return sede
    return None

# --------------------------
# LECTURA DE ARCHIVO (input1.txt formato)
# --------------------------
def leer_archivo(ruta):
    jugadores, equipos, sedes = {}, {}, []
    
    try:
        with open(ruta, 'r') as f:
            txt = f.read()
        
        # Jugadores
        import re
        for var, nom, edad, hab in re.findall(r'(\w+)\s*=.*Jugador\("([^"]+)",\s*(\d+),\s*(\d+)', txt):
            jugadores[var] = Jugador(nom, int(edad), int(hab))
        
        # Equipos
        for var, dep, jugs in re.findall(r'(\w+)\s*=.*Equipo\("([^"]+)",\s*\[([^\]]+)', txt):
            lista_j = [jugadores[j.strip()] for j in jugs.split(',')]
            equipos[var] = Equipo(dep, lista_j)
        
        # Sedes
        for nombre, eqs in re.findall(r'Sede\("([^"]+)",\s*\[([^\]]+)', txt):
            lista_e = [equipos[e.strip()] for e in eqs.split(',')]
            sedes.append(Sede(nombre, lista_e))
        
        return sedes
        
    except Exception:
        return []

# --------------------------
# IMPRESIÓN DE RESULTADOS
# --------------------------
def imprimir_resultados(sedes_ordenadas, ranking, stats):
    for sede in sedes_ordenadas:
        print(f"{sede.nombre}, Rendimiento: {sede.promedio}\n")
        for equipo in sede.equipos:
            print(f"{equipo.deporte}, Rendimiento: {equipo.promedio}")
            print("{" + ", ".join(str(j.id) for j in equipo.jugadores) + "}\n")
    
    print("Ranking Jugadores:")
    print("{" + ", ".join(str(j.id) for j in ranking) + "}\n")
    
    print(f"Equipo con mayor rendimiento: {stats['equipo_mayor'].deporte} {stats['equipo_mayor_sede']}")
    print(f"Equipo con menor rendimiento: {stats['equipo_menor'].deporte} {stats['equipo_menor_sede']}")
    print(f"Jugador con mayor rendimiento: {{ {stats['jugador_mayor_rend'].id} , {stats['jugador_mayor_rend'].nombre} , {stats['jugador_mayor_rend'].rendimiento} }}")
    print(f"Jugador con menor rendimiento: {{ {stats['jugador_menor_rend'].id} , {stats['jugador_menor_rend'].nombre} , {stats['jugador_menor_rend'].rendimiento} }}")
    print(f"Jugador más joven: {{ {stats['jugador_joven'].id} , {stats['jugador_joven'].nombre} , {stats['jugador_joven'].edad} }}")
    print(f"Jugador más veterano: {{ {stats['jugador_veterano'].id} , {stats['jugador_veterano'].nombre} , {stats['jugador_veterano'].edad} }}")
    print(f"Promedio de edad de los jugadores: {stats['promedio_edad']}")
    print(f"Promedio de rendimiento de los jugadores: {stats['promedio_rendimiento']}")

# --------------------------
# EJECUCIÓN PRINCIPAL
# --------------------------
if __name__ == "__main__":
    # Leer datos
    sedes = leer_archivo("input3.txt")
    
    # Procesar
    sedes_ordenadas, ranking = procesar_solucion1(sedes)
    
    # Calcular estadísticas
    stats = calcular_estadisticas(sedes_ordenadas)
    
    # Imprimir resultados
    imprimir_resultados(sedes_ordenadas, ranking, stats)