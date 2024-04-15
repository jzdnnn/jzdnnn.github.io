import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def republikaScrapping():
    url = "https://www.republika.co.id/"
    page = requests.get(url)
    obj = BeautifulSoup(page.content, "html.parser")

    # Ambil Waktu Scrapping
    scrapTime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    # Ambil Data dari Website
    data = []
    element = obj.select('div.col-md-9 div.caption')
    if element:
        for item in element:
            # Ambil Tema Berita
            themeElement = item.select_one('span.kanal-info')
            theme = themeElement.text.strip()

            # Ambil Judul Berita
            titleElement = item.select_one('h3 span')
            title = titleElement.text.strip()

            # Ambil Waktu Publish Berita
            dateElement = item.select_one('div.date')
            date = dateElement.text.strip().split("-")[-1].strip()

            data.append({
                "waktu_scrapping": scrapTime,
                "tema": theme,
                "judul": title,
                "waktu_publish": date
            })

    # Simpan Data dalam File .txt
    with open('headline.txt', 'w') as f:
        for item in data:
            f.write(f"Waktu Scrapping : {item['waktu_scrapping']}\n")
            f.write(f"Tema: {item['tema']}\n")
            f.write(f"Judul: {item['judul']}\n")
            f.write(f"Waktu Publish: {item['waktu_publish']}\n\n")
    print("Data berhasil disimpan dalam file .txt")

    # Simpan Data dalam File .json
    with open('headline.json', 'w') as json_file:
        json.dump(data, json_file, indent=1)
    print("Data berhasil disimpan dalam file .json")

republikaScrapping()

