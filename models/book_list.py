from models.book import *

book1 = Book("Oathbringer", "Brandon Sanderson", "High Fantasy")
book2 = Book("Sapiens", "Yuval Noah Harari", "Anthropology")
book3 = Book("Leviathan Falls", "James S.A. Corey", "Science Fiction")

book_list = [book1, book2, book3]

def add_new_book(new_book):
    book_list.append(new_book)

def delete_book(id):
    book_list.remove(book_list[int(id)])