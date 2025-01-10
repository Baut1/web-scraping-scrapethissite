import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

country_names = [tag.text.strip() for tag in soup.find_all("h3", class_="country-name")]
country_pop = [tag.text.strip() for tag in soup.find_all("span", class_="country-population")]

countries_data = list(zip(country_names, country_pop))

countries_data.sort(key=lambda x: int(x[1].strip()), reverse=True)

for country, population in countries_data[:10]:
  print(f"{country} - population: {population}")