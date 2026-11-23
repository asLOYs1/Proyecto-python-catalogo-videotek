# Matriz de catálogo: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
catalogo = [
    ["Dune: Parte Dos", 2024, 8.8, "Ciencia ficción"],
    [" Oppenheimer", 2023, 8.5, "Drama"],
    ["Spider-Man: A Través del Spider-Verso", 2023, 8.7, "Animación"],
    ["Misión Imposible: Sentencia Mortal", 2023, 7.7, "Acción"],
    ["The Batman", 2022, 7.9, "Acción"],
    ["Sonic 2: La Película", 2022, 6.5, "Aventura"],
    ["Interestelar", 2014, 8.7, "Ciencia ficción"],
    ["Intensamente 2", 2024, 7.8, "Animación"],
]


# Función que cuenta y devuelve la lista de títulos que cumplen los criterios
def evaluar_titulos_populares_actuales(
    matriz_catalogo: list[list], calificacion_minima: float, anio_minimo: int
) -> tuple[int, list[str]]:
  """Devuelve (total, titulos) para los registros que cumplen:

  calificacion >= calificacion_minima y anio >= anio_minimo.
  """
  titulos_cumplen: list[str] = []

  for item in matriz_catalogo:
    if len(item) < 3:
      continue

    titulo = str(item[0]).strip()
    anio = item[1]
    calificacion = item[2]

    if calificacion >= calificacion_minima and anio >= anio_minimo:
      titulos_cumplen.append(titulo)

  return len(titulos_cumplen), titulos_cumplen


# Definición de criterios y ejecución
umbral_calificacion = 8.0
anio_limite = 2023

total_cumplen, lista_titulos = evaluar_titulos_populares_actuales(
    matriz_catalogo=catalogo,
    calificacion_minima=umbral_calificacion,
    anio_minimo=anio_limite,
)

# Salida del resultado
print(
    f"Criterios -> Calificación >= {umbral_calificacion} y Año >= {anio_limite}"
)
print(f"Total de títulos que cumplen ambos criterios: {total_cumplen}")
print("Títulos seleccionados:")
for titulo in lista_titulos:
  print(f"  - {titulo}")