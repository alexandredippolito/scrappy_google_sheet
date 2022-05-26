import requests
from bs4 import BeautifulSoup
import math

url_base = 'https://br.indeed.com/empregos?'


def search_indeed(keyword):
  #cria urls (usando o range)
  urls = []
  for n_page in range(1):
    url = f"{url_base}q={keyword}&limit=50&start={n_page * 50}"
    urls.append(url)
  
    #envia as urls para scrapping
  return scrapping_indeed(urls)

def scrapping_indeed(urls):
  all_jobs = []
  #para cada url recebina faça:
  for url in urls:
    print("começando uma url...")
    #url + request 
    r_indeed = requests.get(url)
    #salva o html no html_indeed
    html_indeed = r_indeed.text
    #faz a sopa
    soup = BeautifulSoup(html_indeed, 'html.parser')
    #filtrar os card. criar lista de cards
    cards = soup.find_all('div', class_="result")
    for card in cards:
      #monta o job
      company = card.find('span', class_='companyName')
      if company == None:
        company = "Não encontrada"
      else:
        company = company.get_text().strip()
      job = {
        'title': card.find('a').find('span').get('title'),
        'company': company,
        'location': card.find('div', class_='companyLocation').string,
        'how_old': card.find('span', class_='date').get_text(),
        'link': f"https://br.indeed.com{card.find('a').get('href')}"
      }
       #add o job na lista all_jobs
      all_jobs.append(job)
  #retorna a lista com todos os jobs
  return all_jobs