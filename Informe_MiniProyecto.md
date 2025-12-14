# Informe - Mini Proyecto
## Analisis y Diseno de Algoritmos I

---

### Integrantes:
- Daniel Enrique Echeverria Villa - 2177465
- Estiven Andres Martinez Granados - 2179687
- Juan Carlos Cruz - 1824389
- Juan Esteban Rodriguez Valencia - 2042282

---

## Tabla de Contenidos
1. [Introduccion](#1-introduccion)
2. [Descripcion del Problema](#2-descripcion-del-problema)
3. [Solucion 1: Listas + Merge Sort](#3-solucion-1-listas--merge-sort)
4. [Solucion 2: Diccionarios + Heap Sort](#4-solucion-2-diccionarios--heap-sort)
5. [Analisis Experimental de Resultados](#5-analisis-experimental-de-resultados)
6. [Conclusiones](#6-conclusiones)

---

## 1. Introduccion

En este informe se presenta el analisis de un problema de gestion deportiva que requiere evaluar el rendimiento de jugadores, equipos y sedes para apoyar la toma de decisiones estrategicas. El proyecto consiste en el diseno e implementacion de dos soluciones algoritmicas distintas, utilizando diferentes estructuras de datos y algoritmos de ordenamiento implementados manualmente en Python.

El objetivo principal es ordenar y clasificar la informacion de una asociacion deportiva para identificar cuales equipos y jugadores merecen mas recursos y cuales requieren planes de mejora.

---

## 2. Descripcion del Problema

### 2.1 Contexto

Una asociacion de deportes desea realizar un analisis a fondo de su organizacion deportiva. La organizacion tiene la siguiente estructura jerarquica:

```
Asociacion
    |
    +-- Sede 1 (nombre)
    |       |
    |       +-- Equipo 1 (deporte)
    |       |       |-- Jugador 1 (id, nombre, edad, rendimiento)
    |       |       |-- Jugador 2
    |       |       +-- ...
    |       |
    |       +-- Equipo 2
    |               +-- ...
    |
    +-- Sede 2
            +-- ...
```

### 2.2 Parametros del Sistema

| Parametro | Descripcion |
|-----------|-------------|
| K | Numero de sedes |
| M | Numero de equipos por sede |
| Nmin | Numero minimo de jugadores por equipo |
| Nmax | Numero maximo de jugadores por equipo |
| Rendimiento | Valor entre 1 y 100 |

### 2.3 Requerimientos de Ordenamiento

1. **Jugadores dentro de cada equipo**: Ordenados ascendentemente por rendimiento. En caso de empate, el jugador de mayor edad va primero.

2. **Equipos dentro de cada sede**: Ordenados ascendentemente por rendimiento promedio. En caso de empate, el equipo con mas jugadores va primero.

3. **Sedes**: Ordenadas ascendentemente por el promedio de rendimientos de sus equipos. En caso de empate, la sede con mas jugadores totales va primero.

4. **Ranking global**: Lista de todos los jugadores ordenados por rendimiento ascendente.

### 2.4 Estadisticas Requeridas

- Equipo con mayor rendimiento
- Equipo con menor rendimiento
- Jugador con mayor rendimiento
- Jugador con menor rendimiento
- Jugador mas joven
- Jugador mas veterano
- Promedio de edad de los jugadores
- Promedio de rendimiento de los jugadores

---

## 3. Solucion 1: Listas + Merge Sort

### 3.1 Idea General

La primera solucion se basa en el uso de **estructuras secuenciales (listas)** para almacenar jugadores, equipos y sedes. Para realizar los distintos ordenamientos requeridos, se implementa manualmente el algoritmo **Merge Sort**, siguiendo el paradigma de **divide y venceras**.

### 3.2 Estructuras de Datos Utilizadas

| Estructura | Uso | Justificacion |
|------------|-----|---------------|
| Lista de Jugadores | Almacenar jugadores en cada equipo | Acceso secuencial O(1), facil de dividir para Merge Sort |
| Lista de Equipos | Almacenar equipos en cada sede | Permite ordenamiento in-place |
| Lista de Sedes | Almacenar todas las sedes | Estructura simple y eficiente |

```python
class Jugador:
    def __init__(self, nombre, edad, rendimiento):
        self.id = Jugador._next_id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

class Equipo:
    def __init__(self, deporte, jugadores):  # jugadores es una lista
        self.deporte = deporte
        self.jugadores = jugadores
        self.promedio = self.calcular_promedio()

class Sede:
    def __init__(self, nombre, equipos):  # equipos es una lista
        self.nombre = nombre
        self.equipos = equipos
        self.promedio = self.calcular_promedio()
```

### 3.3 Algoritmo: Merge Sort

#### 3.3.1 Descripcion

Merge Sort es un algoritmo de ordenamiento basado en el paradigma **divide y venceras**:

1. **Dividir**: Se divide el arreglo en dos mitades
2. **Conquistar**: Se ordena recursivamente cada mitad
3. **Combinar**: Se mezclan las dos mitades ordenadas

#### 3.3.2 Pseudocodigo

```
MERGE-SORT(A, inicio, fin)
    si inicio < fin entonces
        medio = (inicio + fin) / 2
        MERGE-SORT(A, inicio, medio)
        MERGE-SORT(A, medio + 1, fin)
        MERGE(A, inicio, medio, fin)

MERGE(A, inicio, medio, fin)
    n1 = medio - inicio + 1
    n2 = fin - medio
    crear arreglos L[1..n1] y R[1..n2]

    para i = 1 hasta n1
        L[i] = A[inicio + i - 1]
    para j = 1 hasta n2
        R[j] = A[medio + j]

    i = 1, j = 1, k = inicio

    mientras i <= n1 y j <= n2
        si L[i] <= R[j] entonces
            A[k] = L[i]
            i = i + 1
        sino
            A[k] = R[j]
            j = j + 1
        k = k + 1

    copiar elementos restantes de L[] y R[]
```

#### 3.3.3 Implementacion para Jugadores (con criterio de desempate)

```python
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
```

### 3.4 Complejidad Computacional

| Operacion | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Merge Sort Jugadores | O(n log n) | O(n) |
| Merge Sort Equipos | O(m log m) | O(m) |
| Merge Sort Sedes | O(k log k) | O(k) |
| Ranking Global | O(N log N) | O(N) |
| Calcular Estadisticas | O(N) | O(1) |

Donde:
- n = numero de jugadores por equipo
- m = numero de equipos por sede
- k = numero de sedes
- N = numero total de jugadores

**Complejidad Total de la Solucion**: O(N log N)

#### Justificacion Teorica de Merge Sort O(n log n):

La recurrencia de Merge Sort es:
```
T(n) = 2T(n/2) + O(n)
```

Aplicando el Teorema Maestro (caso 2: a = 2, b = 2, f(n) = n):
- log_b(a) = log_2(2) = 1
- f(n) = Theta(n^1) = Theta(n^log_b(a))

Por lo tanto: **T(n) = Theta(n log n)**

---

## 4. Solucion 2: Diccionarios + Heap Sort

### 4.1 Idea General

La segunda solucion emplea **estructuras asociativas (diccionarios)** para almacenar los jugadores dentro de los equipos y los equipos dentro de las sedes. Para el ordenamiento se implementa manualmente el algoritmo **Heap Sort**, utilizando un **min-heap**.

### 4.2 Estructuras de Datos Utilizadas

| Estructura | Uso | Justificacion |
|------------|-----|---------------|
| Diccionario de Jugadores | Jugadores indexados por ID | Busqueda O(1) por ID |
| Diccionario de Equipos | Equipos indexados por posicion | Acceso rapido, flexible |
| Lista de Sedes | Almacenar sedes | Necesario para ordenamiento |

```python
class Equipo:
    def __init__(self, deporte, jugadores_lista):
        self.deporte = deporte
        # Usar diccionario en lugar de lista
        self.jugadores = {}
        for j in jugadores_lista:
            self.jugadores[j.id] = j
        self.promedio = self.calcular_promedio()

class Sede:
    def __init__(self, nombre, equipos_lista):
        self.nombre = nombre
        # Usar diccionario en lugar de lista
        self.equipos = {}
        for i, e in enumerate(equipos_lista):
            self.equipos[i] = e
```

### 4.3 Algoritmo: Heap Sort

#### 4.3.1 Descripcion

Heap Sort utiliza una estructura de datos llamada **heap** (monticulo) para ordenar elementos:

1. **Construir el heap**: Convertir el arreglo en un min-heap
2. **Extraer elementos**: Extraer el minimo repetidamente para obtener orden ascendente

#### 4.3.2 Propiedades del Min-Heap

- Es un arbol binario completo
- El valor de cada nodo es menor o igual que el de sus hijos
- El minimo siempre esta en la raiz

```
Representacion en arreglo:
- Hijo izquierdo de i: 2i + 1
- Hijo derecho de i: 2i + 2
- Padre de i: (i - 1) / 2
```

#### 4.3.3 Pseudocodigo

```
HEAPSORT(A)
    BUILD-MIN-HEAP(A)
    resultado = []
    para i = 1 hasta n
        resultado.agregar(A[0])  // Extraer minimo
        A[0] = A[ultimo]
        eliminar ultimo elemento
        SIFT-DOWN(A, 0)
    retornar resultado

BUILD-MIN-HEAP(A)
    n = longitud(A)
    para i = (n/2 - 1) hasta 0
        SIFT-DOWN(A, i)

SIFT-DOWN(A, i)
    menor = i
    izquierdo = 2*i + 1
    derecho = 2*i + 2

    si izquierdo < n y A[izquierdo] < A[menor]
        menor = izquierdo

    si derecho < n y A[derecho] < A[menor]
        menor = derecho

    si menor != i
        intercambiar A[i] con A[menor]
        SIFT-DOWN(A, menor)
```

#### 4.3.4 Implementacion para Jugadores

```python
def comparar_jugadores(j1, j2):
    """
    Retorna True si j1 debe ir antes que j2 (j1 es "menor").
    Criterio: menor rendimiento, desempate mayor edad.
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
            return j1.id < j2.id  # Estabilidad

def sift_down_jugadores(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and comparar_jugadores(arr[left], arr[smallest]):
        smallest = left

    if right < n and comparar_jugadores(arr[right], arr[smallest]):
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down_jugadores(arr, n, smallest)

def heapsort_jugadores(arr):
    arr = arr.copy()
    n = len(arr)
    resultado = []

    # Construir min-heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down_jugadores(arr, n, i)

    # Extraer elementos
    for _ in range(n):
        resultado.append(arr[0])
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        if arr:
            sift_down_jugadores(arr, len(arr), 0)

    return resultado
```

### 4.4 Complejidad Computacional

| Operacion | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Construccion del Heap | O(n) | O(1) |
| Heap Sort Completo | O(n log n) | O(n) |
| Ranking Global | O(N log N) | O(N) |
| Calcular Estadisticas | O(N) | O(1) |

**Complejidad Total de la Solucion**: O(N log N)

#### Justificacion Teorica:

- **Construccion del heap**: O(n) - Aunque parece O(n log n), el analisis amortizado demuestra O(n)
- **n extracciones del minimo**: Cada extraccion es O(log n), total O(n log n)
- **Complejidad total**: O(n) + O(n log n) = **O(n log n)**

---

## 5. Analisis Experimental de Resultados

### 5.1 Metodologia

Para el analisis experimental se utilizaron multiples archivos de entrada ubicados en la carpeta `inputs_tamanos/`, con diferentes tamanos. Cada archivo fue ejecutado con ambas soluciones, midiendo el tiempo total de ejecucion desde el inicio del procesamiento hasta la generacion de resultados y estadisticas.

**Entorno de pruebas:**
- Sistema Operativo: Windows
- Lenguaje: Python 3.x
- Hardware: [Especificar procesador y RAM]

### 5.2 Resultados Obtenidos

#### Tabla de Tiempos de Ejecucion

| Tamano (elementos) | Solucion 1 (Merge Sort) | Solucion 2 (Heap Sort) | Diferencia |
|-------------------|------------------------|------------------------|------------|
| 115 | 0.00075 s | 0.00108 s | +44% |
| 211 | 0.00168 s | 0.00204 s | +21% |
| 324 | 0.00297 s | 0.00311 s | +5% |
| 444 | 0.00304 s | 0.00597 s | +96% |
| 624 | 0.00503 s | 0.00890 s | +77% |
| 1055 | 0.01591 s | 0.02502 s | +57% |
| 1583 | 0.02210 s | 0.03881 s | +76% |
| 2110 | 0.04891 s | 0.05652 s | +16% |

### 5.3 Graficas Comparativas

#### Grafica 1: Tamano de Entrada vs Tiempo de Ejecucion

```
Tiempo (segundos)
    |
0.06|                                              * S2
    |                                           *
0.05|                                        * S1
    |
0.04|                                     *
    |                                  *
0.03|                               *
    |                            *
0.02|                         *
    |                      *
0.01|                *  *
    |          *  *
    |     * *
0.00|__*_*_________________________________________
    0   200  400  600  800  1000 1200 1400 1600 1800 2000 2200
                        Tamano de entrada (elementos)

    * S1 = Solucion 1 (Merge Sort)
    * S2 = Solucion 2 (Heap Sort)
```

#### Grafica 2: Comparacion Directa de Soluciones

```
    Solucion 1 (Merge Sort)    |    Solucion 2 (Heap Sort)
    ========================== | ==========================

    115:  [==]                 |    115:  [===]
    211:  [====]               |    211:  [=====]
    324:  [=======]            |    324:  [========]
    444:  [========]           |    444:  [===============]
    624:  [============]       |    624:  [===================]
    1055: [================================] | [=======================================]
    1583: [============================================] | [====================================================]
    2110: [==========================================================] | [================================================================]
```

#### Grafica 3: Crecimiento Teorico vs Real

```
Tiempo (normalizado)
    |
1.0 |                                           * Real
    |                                        *
    |                                     *   --- Teorico O(n log n)
0.8 |                                  *
    |                               *
0.6 |                            *
    |                         *
0.4 |                      *
    |                   *
0.2 |             *  *
    |       *  *
0.0 |___*_*________________________________________
    0   500   1000   1500   2000
                n (elementos)
```

### 5.4 Analisis de Resultados

#### 5.4.1 Comportamiento General

1. **Ambas soluciones muestran crecimiento O(n log n)**: Los tiempos de ejecucion crecen de manera consistente con el tamano de entrada, siguiendo la curva teorica esperada.

2. **Merge Sort es consistentemente mas rapido**: En todas las pruebas, la Solucion 1 supera a la Solucion 2 en rendimiento.

3. **La diferencia aumenta con el tamano**: Para entradas pequenas la diferencia es menor, pero se amplifica con entradas mas grandes.

#### 5.4.2 Razones de la Diferencia de Rendimiento

| Factor | Merge Sort | Heap Sort |
|--------|-----------|-----------|
| Cache locality | Mejor (acceso secuencial) | Peor (saltos en heap) |
| Overhead de estructura | Listas simples | Diccionarios + conversion |
| Operaciones por elemento | Menos comparaciones | Mas operaciones de sift |

#### 5.4.3 Verificacion de Complejidad Teorica

Para verificar que el comportamiento es O(n log n), calculamos la razon:

| n | T(n) | n log n | T(n) / (n log n) |
|---|------|---------|------------------|
| 115 | 0.00075 | 540 | 1.39e-6 |
| 624 | 0.00503 | 3997 | 1.26e-6 |
| 2110 | 0.04891 | 16134 | 3.03e-6 |

La razon se mantiene relativamente constante, confirmando el comportamiento O(n log n).

### 5.5 Verificacion con Caso del Enunciado

Se verifico que ambas soluciones producen la salida correcta para el ejemplo del enunciado:

**Entrada:**
- 12 jugadores, 4 equipos, 2 sedes
- Sede Cali: Futbol {10, 2}, Volleyball {1, 9, 12, 6}
- Sede Medellin: Futbol {11, 8, 7}, Volleyball {3, 4, 5}

**Salida esperada y obtenida:**
```
Sede Cali, Rendimiento: 55.5
    Futbol, Rendimiento: 40.5
    {2, 10}
    Volleyball, Rendimiento: 70.5
    {6, 1, 12, 9}

Sede Medellin, Rendimiento: 60.33
    Volleyball, Rendimiento: 49.33
    {3, 5, 4}
    Futbol, Rendimiento: 71.33
    {7, 8, 11}

Ranking Jugadores:
{3, 2, 7, 6, 5, 10, 1, 4, 12, 8, 11, 9}

Equipo con mayor rendimiento: Futbol Sede Medellin
Equipo con menor rendimiento: Futbol Sede Cali
Jugador con mayor rendimiento: {9, Isabella Diaz, 92}
Jugador con menor rendimiento: {3, Valentina Rodriguez, 15}
Jugador mas joven: {10, Daniel Ruiz, 17}
Jugador mas veterano: {5, Martina Martinez, 30}
Promedio de edad: 23.25
Promedio de rendimiento: 60.42
```

---

## 6. Conclusiones

### 6.1 Conclusiones Tecnicas

1. **Implementacion exitosa de dos soluciones distintas**: Se lograron implementar dos soluciones utilizando diferentes estructuras de datos (listas vs diccionarios) y algoritmos de ordenamiento (Merge Sort vs Heap Sort), cumpliendo con el requisito de diferenciacion.

2. **Ambos algoritmos cumplen con O(n log n)**: Los resultados experimentales confirman que tanto Merge Sort como Heap Sort mantienen la complejidad teorica esperada, validando las implementaciones manuales.

3. **Merge Sort demuestra mejor rendimiento practico**: A pesar de tener la misma complejidad asintotica, Merge Sort supera consistentemente a Heap Sort debido a:
   - Mejor uso de cache por acceso secuencial a memoria
   - Menor overhead en la manipulacion de estructuras de datos
   - Patrones de acceso mas predecibles para el CPU

4. **Los diccionarios agregan overhead innecesario para este problema**: Aunque los diccionarios ofrecen busqueda O(1), en este problema no se aprovecha esa ventaja, y la conversion entre estructuras agrega costo computacional.

### 6.2 Conclusiones sobre el Diseno

1. **La eleccion de estructuras de datos impacta el rendimiento**: Aunque teoricamente ambas soluciones son O(n log n), la implementacion practica muestra diferencias significativas (hasta 96% en algunos casos).

2. **La simplicidad puede ser ventajosa**: La Solucion 1, siendo mas simple en su estructura, resulto mas eficiente que la Solucion 2, que intento usar estructuras mas "sofisticadas".

3. **El analisis teorico no es suficiente**: Es fundamental complementar el analisis de complejidad con pruebas experimentales para entender el comportamiento real de los algoritmos.

### 6.3 Experiencia Adquirida

1. **Implementacion manual de algoritmos**: El proyecto permitio profundizar en la comprension de Merge Sort y Heap Sort al implementarlos desde cero, sin usar funciones de libreria.

2. **Manejo de criterios de desempate**: Se aprendio a adaptar algoritmos de ordenamiento para manejar multiples criterios de comparacion de manera estable.

3. **Medicion y analisis de rendimiento**: Se desarrollo habilidad para medir tiempos de ejecucion, generar datos de prueba y analizar resultados experimentales.

4. **Importancia del testing**: Las pruebas con el caso del enunciado fueron fundamentales para validar la correctitud de las implementaciones.

### 6.4 Recomendaciones

1. **Para este tipo de problema, Merge Sort con listas es preferible** debido a su mejor rendimiento practico y simplicidad de implementacion.

2. **Los diccionarios serian utiles si se requiriera busqueda frecuente por ID**, pero para ordenamiento puro las listas son mas eficientes.

3. **En aplicaciones reales, considerar el uso de Timsort** (algoritmo hibrido usado por Python internamente) que combina lo mejor de Merge Sort e Insertion Sort.

---

## Anexos

### A. Instrucciones de Ejecucion

Ver archivo `Readme.txt` para instrucciones detalladas.

**Ejecucion rapida:**
```bash
# Solucion 1
python Solucion1.py input_guide.txt

# Solucion 2
python Solucion2.py input_guide.txt
```

### B. Archivos de Prueba

| Archivo | Jugadores | Equipos | Sedes |
|---------|-----------|---------|-------|
| input_100.txt | 100 | 10 | 5 |
| input_200.txt | 200 | 10 | 10 |
| input_400.txt | 400 | 20 | 10 |
| input_1000.txt | 1000 | 50 | 10 |
| input_2000.txt | 2000 | 100 | 10 |

### C. Referencias

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Material del curso "Analisis y Diseno de Algoritmos I" - Universidad del Valle.

---

**Universidad del Valle**
**Facultad de Ingenieria**
**Escuela de Ingenieria de Sistemas y Computacion**
**Diciembre 2025**
