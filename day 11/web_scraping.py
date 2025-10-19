import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html')
soup = bs4.BeautifulSoup(resultado.text, 'lxml')

print(soup.select('title')[0].getText())

parrafo_especial = soup.select('p')[3].getText()
print(parrafo_especial)

columna_lateral = soup.select('.widget-content h3')

for h3 in columna_lateral:
    print(h3.getText())