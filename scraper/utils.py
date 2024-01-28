import requests
from bs4 import BeautifulSoup
from .models import WebScrape
import re

def scrap_wiki(url):
   res = requests.get(url)
   print("From utils:",res)
   if res.status_code==200:
      doc = BeautifulSoup(res.text,"html.parser")
      title = doc.title.string.replace(" - Wikipedia", "")
      info_box={}
      info_box_table = doc.find('table',class_='infobox')
      if info_box_table:
        rows = info_box_table.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header:
                header_text = header.text.strip()
                data_cell = row.find('td')
                if data_cell:
                   data_text = re.sub(r'\[\d+\]', '', data_cell.text.strip())                
                   info_box[header_text ] = data_text.replace('\n','')
      
      wiki_page = WebScrape.objects.create(url=url, title=title, info=info_box)
      wiki_page.save()
      return wiki_page.id            
   return False

  

