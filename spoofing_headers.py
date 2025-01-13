import requests
from bs4 import BeautifulSoup

# URL base y parsms
BASE_URL = "https://www.scrapethissite.com/pages/advanced/"
PARAMS = "?gotcha=headers"
URL = BASE_URL + PARAMS

# headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.scrapethissite.com/",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}

def main():
  response = requests.get(URL, headers=HEADERS)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      message = soup.find("div", class_="col-md-4 col-md-offset-4").text.strip()
      print(message)
  else:
     print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()