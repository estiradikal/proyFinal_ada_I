import sys
import time
import re

# --------------------------
# CLASES BASICAS (usando diccionarios)
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
    def __init__(self, deporte, jugadores_lista):
        self.deporte = deporte
        # Usar diccionario en lugar de lista
        self.jugadores = {}
        for j in jugadores_lista:
            self.jugadores[j.id] = j
        self.promedio = self.calcular_promedio()

    def calcular_promedio(self):
        if not self.jugadores:
            return 0
        return sum(j.rendimiento for j in self.jugadores.values()) / len(self.jugadores)

    def obtener_jugadores_lista(self):
        return list(self.jugadores.values())

    def __repr__(self):
        return f"{self.deporte}"

class Sede:
    def __init__(self, nombre, equipos_lista):
        self.nombre = nombre
        # Usar diccionario en lugar de lista
        self.equipos = {}
        for i, e in enumerate(equipos_lista):
            self.equipos[i] = e
        self.promedio = self.calcular_promedio()
        self.total_jugadores = sum(len(e.jugadores) for e in self.equipos.values())

    def calcular_promedio(self):
        if not self.equipos:
            return 0
        return sum(e.promedio for e in self.equipos.values()) / len(self.equipos)

    def obtener_equipos_lista(self):
        return list(self.equipos.values())

    def __repr__(self):
        return f"{self.nombre}"

# --------------------------
# HEAPSORT MANUAL (sin usar heapq)
# --------------------------

def comparar_jugadores(j1, j2):
    """
    Compara dos jugadores para min-heap.
    Retorna True si j1 debe ir antes que j2 (j1 es "menor").
    Criterio: menor rendimiento, desempate mayor edad, desempate menor ID.
    """
    if j1.rendimiento < j2.rendimiento:
        return True
    elif j1.rendimiento > j2.rendimiento:
        return False
    else:
        # Mismo rendimiento: mayor edad primero
        if j1.edad > j2.edad:
            return True
        elif j1.edad < j2.edad:
            return False
        else:
            # Misma edad: menor ID primero (para estabilidad)
            return j1.id < j2.id

def sift_down_jugadores(arr, n, i):
    """
    Mantiene la propiedad de min-heap para jugadores.
    Criterio: menor rendimiento primero, desempate por mayor edad, desempate por menor ID.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Comparar con hijo izquierdo
    if left < n and comparar_jugadores(arr[left], arr[smallest]):
        smallest = left

    # Comparar con hijo derecho
    if right < n and comparar_jugadores(arr[right], arr[smallest]):
        smallest = right

    # Si el menor no es el padre, intercambiar y continuar
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down_jugadores(arr, n, smallest)

def heapify_jugadores(arr):
    """Construye un min-heap desde un array de jugadores."""
    n = len(arr)
    # Empezar desde el ultimo nodo no-hoja
    for i in range(n // 2 - 1, -1, -1):
        sift_down_jugadores(arr, n, i)

def heapsort_jugadores(arr):
    """
    HeapSort para ordenar jugadores por rendimiento ascendente.
    Desempate: mayor edad primero.
    """
    if len(arr) <= 1:
        return arr

    arr = arr.copy()
    n = len(arr)
    resultado = []

    # Construir min-heap
    heapify_jugadores(arr)

    # Extraer elementos uno por uno
    for _ in range(n):
        # El minimo esta en la raiz
        resultado.append(arr[0])
        # Mover el ultimo elemento a la raiz
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        if arr:
            sift_down_jugadores(arr, len(arr), 0)

    return resultado

# --------------------------
# HEAPSORT PARA EQUIPOS
# --------------------------

def sift_down_equipos(arr, n, i):
    """
    Min-heap para equipos.
    Criterio: menor promedio primero, desempate por mas jugadores.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        if arr[left].promedio < arr[smallest].promedio:
            smallest = left
        elif arr[left].promedio == arr[smallest].promedio:
            if len(arr[left].jugadores) > len(arr[smallest].jugadores):
                smallest = left

    if right < n:
        if arr[right].promedio < arr[smallest].promedio:
            smallest = right
        elif arr[right].promedio == arr[smallest].promedio:
            if len(arr[right].jugadores) > len(arr[smallest].jugadores):
                smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down_equipos(arr, n, smallest)

def heapify_equipos(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down_equipos(arr, n, i)

def heapsort_equipos(arr):
    """HeapSort para ordenar equipos por promedio ascendente."""
    if len(arr) <= 1:
        return arr

    arr = arr.copy()
    n = len(arr)
    resultado = []

    heapify_equipos(arr)

    for _ in range(n):
        resultado.append(arr[0])
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        if arr:
            sift_down_equipos(arr, len(arr), 0)

    return resultado

# --------------------------
# HEAPSORT PARA SEDES
# --------------------------

def sift_down_sedes(arr, n, i):
    """
    Min-heap para sedes.
    Criterio: menor promedio primero, desempate por mas jugadores totales.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        if arr[left].promedio < arr[smallest].promedio:
            smallest = left
        elif arr[left].promedio == arr[smallest].promedio:
            if arr[left].total_jugadores > arr[smallest].total_jugadores:
                smallest = left

    if right < n:
        if arr[right].promedio < arr[smallest].promedio:
            smallest = right
        elif arr[right].promedio == arr[smallest].promedio:
            if arr[right].total_jugadores > arr[smallest].total_jugadores:
                smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down_sedes(arr, n, smallest)

def heapify_sedes(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down_sedes(arr, n, i)

def heapsort_sedes(arr):
    """HeapSort para ordenar sedes por promedio ascendente."""
    if len(arr) <= 1:
        return arr

    arr = arr.copy()
    n = len(arr)
    resultado = []

    heapify_sedes(arr)

    for _ in range(n):
        resultado.append(arr[0])
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        if arr:
            sift_down_sedes(arr, len(arr), 0)

    return resultado

# --------------------------
# PROCESAMIENTO
# --------------------------
def procesar_solucion2(sedes):
    # 1. Ordenar jugadores dentro de cada equipo usando HeapSort
    for sede in sedes:
        for equipo in sede.obtener_equipos_lista():
            jugadores_ordenados = heapsort_jugadores(equipo.obtener_jugadores_lista())
            # Reconstruir diccionario ordenado
            equipo.jugadores = {}
            for j in jugadores_ordenados:
                equipo.jugadores[j.id] = j
            equipo.promedio = equipo.calcular_promedio()

    # 2. Ordenar equipos dentro de cada sede usando HeapSort
    for sede in sedes:
        equipos_ordenados = heapsort_equipos(sede.obtener_equipos_lista())
        sede.equipos = {}
        for i, e in enumerate(equipos_ordenados):
            sede.equipos[i] = e
        sede.promedio = sede.calcular_promedio()
        sede.total_jugadores = sum(len(e.jugadores) for e in sede.equipos.values())

    # 3. Ordenar sedes usando HeapSort
    sedes_ordenadas = heapsort_sedes(sedes)

    # 4. Ranking global de jugadores
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.obtener_equipos_lista():
            todos_jugadores.extend(equipo.obtener_jugadores_lista())
    ranking = heapsort_jugadores(todos_jugadores)

    return sedes_ordenadas, ranking

# --------------------------
# ESTADISTICAS
# --------------------------
def calcular_estadisticas(sedes):
    todos_jugadores = []
    for sede in sedes:
        for equipo in sede.obtener_equipos_lista():
            todos_jugadores.extend(equipo.obtener_jugadores_lista())

    if not todos_jugadores:
        return {}

    jugador_mayor_rend = max(todos_jugadores, key=lambda j: j.rendimiento)
    jugador_menor_rend = min(todos_jugadores, key=lambda j: j.rendimiento)
    jugador_joven = min(todos_jugadores, key=lambda j: j.edad)
    jugador_veterano = max(todos_jugadores, key=lambda j: j.edad)

    promedio_edad = sum(j.edad for j in todos_jugadores) / len(todos_jugadores)
    promedio_rendimiento = sum(j.rendimiento for j in todos_jugadores) / len(todos_jugadores)

    # Equipo con mayor y menor rendimiento
    todos_equipos = [eq for sede in sedes for eq in sede.obtener_equipos_lista()]
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
        if equipo in sede.obtener_equipos_lista():
            return sede
    return None

# --------------------------
# LECTURA DE ARCHIVO
# --------------------------
def leer_archivo(ruta):
    jugadores, equipos, sedes = {}, {}, []

    try:
        with open(ruta, 'r') as f:
            lineas = f.readlines()
            lineas_no_vacias = len([l for l in lineas if l.strip()])
            txt = ''.join(lineas)

        # Jugadores
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

        return sedes, lineas_no_vacias

    except Exception:
        return [], 0

# --------------------------
# IMPRESION DE RESULTADOS
# --------------------------
def imprimir_resultados(sedes_ordenadas, ranking, stats):
    for sede in sedes_ordenadas:
        print(f"{sede.nombre}, Rendimiento: {sede.promedio}\n")
        for equipo in sede.obtener_equipos_lista():
            print(f"{equipo.deporte}, Rendimiento: {equipo.promedio}")
            print("{" + ", ".join(str(j.id) for j in equipo.obtener_jugadores_lista()) + "}\n")

    print("Ranking Jugadores:")
    print("{" + ", ".join(str(j.id) for j in ranking) + "}\n")

    print(f"Equipo con mayor rendimiento: {stats['equipo_mayor'].deporte} {stats['equipo_mayor_sede']}")
    print(f"Equipo con menor rendimiento: {stats['equipo_menor'].deporte} {stats['equipo_menor_sede']}")
    print(f"Jugador con mayor rendimiento: {{ {stats['jugador_mayor_rend'].id} , {stats['jugador_mayor_rend'].nombre} , {stats['jugador_mayor_rend'].rendimiento} }}")
    print(f"Jugador con menor rendimiento: {{ {stats['jugador_menor_rend'].id} , {stats['jugador_menor_rend'].nombre} , {stats['jugador_menor_rend'].rendimiento} }}")
    print(f"Jugador mas joven: {{ {stats['jugador_joven'].id} , {stats['jugador_joven'].nombre} , {stats['jugador_joven'].edad} }}")
    print(f"Jugador mas veterano: {{ {stats['jugador_veterano'].id} , {stats['jugador_veterano'].nombre} , {stats['jugador_veterano'].edad} }}")
    print(f"Promedio de edad de los jugadores: {stats['promedio_edad']}")
    print(f"Promedio de rendimiento de los jugadores: {stats['promedio_rendimiento']}")

def imprimir_analisis_tiempo(tiempo, longitud):
    print(f"Tiempo de ejecucion para {longitud} elementos: {tiempo} segundos")

# --------------------------
# EJECUCION PRINCIPAL
# --------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python Solucion2.py <archivo_entrada>")
        sys.exit(1)

    archivo = sys.argv[1]
    sedes, tamano_entrada = leer_archivo(archivo)

    ## EMPIEZA CONTEO DE TIEMPO
    start_time = time.time()

    # Procesar con HeapSort
    sedes_ordenadas, ranking = procesar_solucion2(sedes)

    # Calcular estadisticas
    stats = calcular_estadisticas(sedes_ordenadas)

    ## TERMINA CONTEO DE TIEMPO
    end_time = time.time()

    ## Calcular tiempo transcurrido
    elapsed_time = end_time - start_time

    # Imprimir resultados
    imprimir_resultados(sedes_ordenadas, ranking, stats)

    imprimir_analisis_tiempo(elapsed_time, tamano_entrada)
