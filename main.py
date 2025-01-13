import requests
from bs4 import BeautifulSoup

# URL
url = "https://www.scrapethissite.com/pages/simple/"

# Obtener datos
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer datos
countries_data = [
    (tag.text.strip(), int(pop.text.strip()))
    for tag, pop in zip(
        soup.find_all("h3", class_="country-name"),
        soup.find_all("span", class_="country-population")
    )
]

# Ordenar
top_countries = sorted(countries_data, key=lambda x: x[1], reverse=True)[:10]

# Imprimir
for country, population in top_countries:
    print(f"{country} - population: {population:,.0f}".replace(",", "."))