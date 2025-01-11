import requests
from bs4 import BeautifulSoup

base_url = "https://www.scrapethissite.com/pages/forms/"
query = "New York"

# Almacenar los resultados
all_seasons_data = []

# Comenzar desde la primera página
page_num = 1

while True:
    # URL
    if page_num == 1:
        url = f"{base_url}?q={query.replace(' ', '+')}"
    else:
        url = f"{base_url}?page_num={page_num}&q={query.replace(' ', '+')}"

    # solicitud http
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer datos
    names = [tag.text.strip() for tag in soup.find_all("td", class_="name")]
    years = [tag.text.strip() for tag in soup.find_all("td", class_="year")]
    win_rates = [tag.text.strip() for tag in soup.find_all("td", class_="pct")]

    # Si no hay más datos, salir del bucle
    if not names:
        break

    # Combinar los datos y agregar a la lista general
    seasons_data = list(zip(names, years, win_rates))
    all_seasons_data.extend(seasons_data)

    # siguiente página
    page_num += 1

# ordenar
all_seasons_data.sort(key=lambda x: float(x[2].strip()), reverse=True)

# Imprimir
for name, year, win_rate in all_seasons_data[:20]:
    print(f"{name} {year} - wr%: {win_rate}")
