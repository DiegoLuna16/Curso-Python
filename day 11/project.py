import bs4
import requests

#Crear una url sin numero de pagina
base_url = 'https://books.toscrape.com/catalogue/category/books_1/page-1.html'

#lista de titulos con 4 0 5 estrellas
titles_high_rating = []

#iterar paginas

for page in range(1,11):
    
    #crear sopa para cada pagina
    result = requests.get(base_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')    
    
    #seleccionar datos de los libros
    books = soup.select('.product_pod')
    for book in books:
        
        #comprobar que tiene 4 o 5 estrellas
        if book.select('.star-rating.Four') or book.select('.star-rating.Five'):
            #guardar libro en variable
            book_title = book.select('h3')[0].text
            
            #agregar libro a la lista
            titles_high_rating.append(book_title)


print(f"\nTotal de libros con 4 o 5 estrellas: {len(titles_high_rating)}")
