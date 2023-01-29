import unittest
from models.book import Book
from models.book_list import *

class TestBook(unittest.TestCase):
    def setUp(self):

        self.book1 = Book("Oathbringer", "Brandon Sanderson", "High Fantasy", True)
        self.book2 = Book("Sapiens", "Yuval Noah Harari", "Anthropology", False)
        self.book3 = Book("Leviathan Falls", "James S.A. Corey", "Science Fiction", True)
        self.new_book = Book("Mistborn", "Brandon Sanderson", "High Fantasy", True)

        book_list = [self.book1, self.book2, self.book3]

    def test_add_new_book(self):
        expected = add_new_book(self.new_book)
        self.assertEqual("Mistborn", book_list[3].title)