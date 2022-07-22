import requests

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"

def get_books():
    books = requests.get(url+endpoint_book)
    return books.json()['books']
books = get_books()
books

def get_category_list(books):
    return {book['subject'].title() for book in books}
get_category_list(books)