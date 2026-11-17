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

    def test_cannot_remove_loaned_book(self):
        self.library.add_reader(10, "Иван")
        self.library.loan_book(10, 1)

        with self.assertRaises(ValueError):
            self.library.remove_book(1)

    def test_add_book_validation(self):
        with self.assertRaises(ValueError):
            self.library.add_book(1, "Другая книга", "Автор")

        with self.assertRaises(ValueError):
            self.library.add_book(2, "", "Автор")

        with self.assertRaises(ValueError):
            self.library.add_book(3, "Книга", "Автор", 0)

    def test_search_empty_query(self):
        self.assertEqual(self.library.search_books(""), [])
        self.assertEqual(self.library.search_books("   "), [])

    def test_search_case_insensitive(self):
        self.assertEqual(len(self.library.search_books("ЧИСТЫЙ")), 1)
    
    def test_add_reader_validation(self):
        with self.assertRaises(ValueError):
            self.library.add_reader(0, "Иван")

        with self.assertRaises(ValueError):
            self.library.add_reader(11, "")

        with self.assertRaises(ValueError):
            self.library.add_reader(10, "Иван")
            self.library.add_reader(10, "Пётр")

    def test_loan_nonexistent_book(self):
        self.library.add_reader(10, "Иван")

        with self.assertRaises(ValueError):
            self.library.loan_book(10, 999)

    def test_loan_without_reader(self):
        with self.assertRaises(ValueError):
            self.library.loan_book(999, 1)

    def test_count_books(self):
        library = Library()
        library.add_book(1, "Book 1", "Author 1")
        library.add_book(2, "Book 2", "Author 2")
        self.assertEqual(library.count_books(), 2)

    def test_get_available_books(self):
        self.library.add_book(1, "Book 1", "Author 1", 2)
        self.library.add_book(2, "Book 2", "Author 2", 1)
        self.library.loan_book(10, 1)
        available = self.library.get_available_books()
        self.assertEqual(len(available), 2)
        self.assertEqual(available[0][1]["available"], 1)


if __name__ == "__main__":
    unittest.main()