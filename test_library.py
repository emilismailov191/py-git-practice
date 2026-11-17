import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book(1, "Чистый код", "Роберт Мартин", 2)

    def test_add_and_list(self):
        self.assertEqual(len(self.library.list_books()), 1)

    def test_search(self):
        self.assertEqual(len(self.library.search_books("чистый")), 1)

    def test_availability_and_loan_return(self):
        self.library.add_reader(10, "Иван")
        self.assertTrue(self.library.is_available(1))
        self.library.loan_book(10, 1)
        self.assertEqual(self.library.books[1]["available"], 1)
        self.library.return_book(10, 1)
        self.assertEqual(self.library.books[1]["available"], 2)

    def test_remove(self):
        self.assertTrue(self.library.remove_book(1))
        self.assertFalse(self.library.is_available(1))


if __name__ == "__main__":
    unittest.main()
