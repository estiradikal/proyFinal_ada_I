================================================================================
                         MINI PROYECTO - ADA I
                    Asociacion de Deportes - Ordenamiento
================================================================================

INTEGRANTES:
- Daniel Enrique Echeverria Villa - 2177465
- Estiven Andres Martinez Granados - 2179687
- Juan Carlos Cruz - 1824389
- Juan Esteban Rodriguez Valencia - 2042282

================================================================================
                           DESCRIPCION DEL PROYECTO
================================================================================

Este proyecto implementa dos soluciones algoritmicas para el problema de
ordenamiento y analisis de rendimiento de una asociacion deportiva. El sistema
permite ordenar jugadores, equipos y sedes segun criterios de rendimiento,
ademas de generar estadisticas relevantes.

================================================================================
                           ARCHIVOS DEL PROYECTO
================================================================================

ARCHIVOS PRINCIPALES:
---------------------
- Solucion1.py          : Implementacion usando Listas + Merge Sort
- Solucion2.py          : Implementacion usando Diccionarios + Heap Sort
- Readme.txt            : Este archivo con instrucciones

ARCHIVOS DE ENTRADA (PRUEBAS):
------------------------------
- input1.txt            : Caso de prueba basico (12 jugadores)
- input2.txt            : Caso de prueba alternativo
- input3.txt            : Caso de prueba adicional
- input_guide.txt       : Caso de prueba del enunciado

CARPETA inputs_tamanos/:
------------------------
- input_100.txt         : Prueba con 100 elementos
- input_200.txt         : Prueba con 200 elementos
- input_300.txt         : Prueba con 300 elementos
- input_400.txt         : Prueba con 400 elementos
- input_600.txt         : Prueba con 600 elementos
- input_1000.txt        : Prueba con 1000 elementos
- input_1500.txt        : Prueba con 1500 elementos
- input_2000.txt        : Prueba con 2000 elementos

CARPETA archivos_generados/:
----------------------------
- csv_parser.py         : Script auxiliar para generar datos
- RandomData.csv        : Datos aleatorios generados
- jugadores.txt         : Lista de jugadores generados
- equipos.txt           : Lista de equipos generados
- sedes.txt             : Lista de sedes generadas

DOCUMENTACION:
--------------
- Informe - Mini Proyecto.pdf : Informe completo del proyecto

================================================================================
                         REQUISITOS DEL SISTEMA
================================================================================

- Python 3.6 o superior
- No requiere librerias externas (solo modulos estandar: sys, time, re)

Para verificar la version de Python:
    python --version
    o
    python3 --version

================================================================================
                       INSTRUCCIONES DE EJECUCION
================================================================================

SOLUCION 1 (Listas + Merge Sort):
---------------------------------
Abrir una terminal/consola en la carpeta del proyecto y ejecutar:

    Windows:
        python Solucion1.py <archivo_entrada>

    Linux/Mac:
        python3 Solucion1.py <archivo_entrada>

Ejemplos:
    python Solucion1.py input1.txt
    python Solucion1.py input_guide.txt
    python Solucion1.py inputs_tamanos/input_100.txt
    python Solucion1.py inputs_tamanos/input_2000.txt


SOLUCION 2 (Diccionarios + Heap Sort):
--------------------------------------
Abrir una terminal/consola en la carpeta del proyecto y ejecutar:

    Windows:
        python Solucion2.py <archivo_entrada>

    Linux/Mac:
        python3 Solucion2.py <archivo_entrada>

Ejemplos:
    python Solucion2.py input1.txt
    python Solucion2.py input_guide.txt
    python Solucion2.py inputs_tamanos/input_100.txt
    python Solucion2.py inputs_tamanos/input_2000.txt

================================================================================
                           FORMATO DE ENTRADA
================================================================================

Los archivos de entrada deben seguir el siguiente formato:

1. Definicion de jugadores:
   j1 = Jugador.Jugador("Nombre", edad, rendimiento)

   Donde:
   - Nombre: cadena de texto
   - edad: entero positivo
   - rendimiento: entero entre 1 y 100

2. Definicion de equipos:
   e1 = Equipo.Equipo("Deporte", [j1, j2, j3])

   Donde:
   - Deporte: nombre del deporte (ej: "Futbol", "Volleyball")
   - Lista de jugadores previamente definidos

3. Definicion de sedes:
   s1 = Sede.Sede("Nombre Sede", [e1, e2])

   Donde:
   - Nombre Sede: nombre de la sede
   - Lista de equipos previamente definidos

EJEMPLO:
--------
j1 = Jugador.Jugador("Sofia Garcia", 21, 66)
j2 = Jugador.Jugador("Alejandro Torres", 27, 24)

e1 = Equipo.Equipo("Futbol", [j1, j2])

s1 = Sede.Sede("Sede Cali", [e1])

================================================================================
                           FORMATO DE SALIDA
================================================================================

El programa genera la siguiente salida:

1. Lista de sedes ordenadas con sus equipos y jugadores
2. Ranking global de todos los jugadores
3. Estadisticas:
   - Equipo con mayor rendimiento
   - Equipo con menor rendimiento
   - Jugador con mayor rendimiento
   - Jugador con menor rendimiento
   - Jugador mas joven
   - Jugador mas veterano
   - Promedio de edad de los jugadores
   - Promedio de rendimiento de los jugadores
4. Tiempo de ejecucion del algoritmo

================================================================================
                        DESCRIPCION DE SOLUCIONES
================================================================================

SOLUCION 1 - Listas + Merge Sort:
---------------------------------
- Estructuras: Listas de Python para almacenar jugadores, equipos y sedes
- Algoritmo: Merge Sort implementado manualmente (divide y venceras)
- Complejidad: O(n log n) para ordenamiento

SOLUCION 2 - Diccionarios + Heap Sort:
--------------------------------------
- Estructuras: Diccionarios para jugadores en equipos y equipos en sedes
- Algoritmo: Heap Sort implementado manualmente (min-heap)
- Complejidad: O(n log n) para ordenamiento

================================================================================
                              NOTAS ADICIONALES
================================================================================

- Los algoritmos de ordenamiento fueron implementados manualmente sin usar
  funciones de libreria como sorted() o heapq.

- El tiempo de ejecucion mostrado corresponde unicamente al procesamiento
  y ordenamiento de datos, excluyendo la lectura del archivo.

- Para pruebas de rendimiento, se recomienda usar los archivos en la carpeta
  inputs_tamanos/ con diferentes tamanios.

================================================================================
                                 CONTACTO
================================================================================

Universidad del Valle
Curso: Analisis y Diseno de Algoritmos I
Profesor: Jesus Alexander Aranda Bueno
Monitor: Samuel Galindo Cuevas

Fecha de entrega: 13 de Diciembre de 2025

================================================================================
