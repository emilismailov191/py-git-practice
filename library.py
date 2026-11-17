class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}
        self.loans = {}

    def add_book(self, book_id, title, author, copies=1):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("ID книги должен быть положительным числом")
        if book_id in self.books:
            raise ValueError("Книга с таким ID уже существует")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги не может быть пустым")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        if not isinstance(copies, int) or copies < 1:
            raise ValueError("Количество экземпляров должно быть положительным числом")

        self.books[book_id] = {
            "title": title.strip(),
            "author": author.strip(),
            "copies": copies,
            "available": copies,
        }

    def remove_book(self, book_id):
        if book_id not in self.books:
            return False
        if self.books[book_id]["available"] != self.books[book_id]["copies"]:
            raise ValueError("Нельзя удалить книгу, пока экземпляры выданы")
        del self.books[book_id]
        return True

    def search_books(self, title):
        if not isinstance(title, str) or not title.strip():
            return []

        query = title.strip().casefold()
        return [
            (book_id, book.copy())
            for book_id, book in self.books.items()
            if query in book["title"].casefold()
        ]

    def list_books(self):
        return [(book_id, book.copy()) for book_id, book in self.books.items()]

    def is_available(self, book_id):
        return book_id in self.books and self.books[book_id]["available"] > 0

    def add_reader(self, reader_id, name):
        if not isinstance(reader_id, int) or reader_id <= 0:
            raise ValueError("ID читателя должен быть положительным числом")
        if reader_id in self.readers:
            raise ValueError("Читатель уже существует")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя читателя не может быть пустым")

        self.readers[reader_id] = name.strip()

    def loan_book(self, reader_id, book_id):
        if reader_id not in self.readers:
            raise ValueError("Читатель не найден")
        if book_id not in self.books:
            raise ValueError("Книга не найдена")
        if not self.is_available(book_id):
            raise ValueError("Нет доступных экземпляров")

        self.books[book_id]["available"] -= 1
        self.loans.setdefault(reader_id, []).append(book_id)

    def return_book(self, reader_id, book_id):
        if reader_id not in self.loans or book_id not in self.loans[reader_id]:
            raise ValueError("Эта книга не числится за читателем")

        self.loans[reader_id].remove(book_id)

        if book_id in self.books:
            self.books[book_id]["available"] += 1

    def count_books(self):
        return len(self.books)

    def get_available_books(self):
        return [
            (book_id, book.copy())
            for book_id, book in self.books.items()
            if book['available'] > 0
        ]
