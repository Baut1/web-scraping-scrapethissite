import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://www.scrapethissite.com/pages/frames/"
iframe_param = "?frame=i"
query_param = "&family="

# Solicitud inicial
response = requests.get(base_url + iframe_param)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

# nombres
soup = BeautifulSoup(response.text, 'html.parser')
names = [tag.text.strip() for tag in soup.find_all("h3", class_="family-name")]

# Obtener detalles
for name in names:
    detail_url = base_url + iframe_param + query_param + name
    response = requests.get(detail_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        description = soup.find("div", class_="turtle-family-detail").find("p", class_="lead").text.strip()
        print(f"{name}: {description}\n")
    else:
        print(f"Error al obtener detalles para {name}")