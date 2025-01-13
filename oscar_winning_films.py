import requests

# Año a buscar
year = "2012"

# URL
url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={year}"

# Solicitud API
response = requests.get(url)

if response.status_code == 200:
    movies = response.json()  # Convertir la respuesta a JSON
else:
    print(f"Error: {response.status_code}")
    movies = []

# Ordenar películas
movies.sort(key=lambda m: (m['awards'], m['nominations']), reverse=True)

# Mostrar año
print(f"Año: {year}\n")

# 10 películas mas ganadoras
for movie in movies[:10]:
    if 'best_picture' in movie:
        best_picture = movie['title']
    print(f"{movie['title']}, {movie['nominations']} nominaciones, {movie['awards']} premios")

# mejor pelicula
print(f"\nGanadora mejor pelicula: {best_picture}")
