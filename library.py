class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}
        self.loans = {}

    def add_book(self, book_id, title, author, copies=1):
        if book_id in self.books:
            raise ValueError("Книга с таким ID уже существует")
        if not title.strip() or copies < 1:
            raise ValueError("Название и количество экземпляров должны быть корректными")
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
        query = title.casefold()
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
        if reader_id in self.readers:
            raise ValueError("Читатель уже существует")
        self.readers[reader_id] = name

    def loan_book(self, reader_id, book_id):
        if reader_id not in self.readers:
            raise ValueError("Читатель не найден")
        if not self.is_available(book_id):
            raise ValueError("Нет доступных экземпляров")
        self.books[book_id]["available"] -= 1
        self.loans.setdefault(reader_id, []).append(book_id)

    def return_book(self, reader_id, book_id):
        if reader_id not in self.loans or book_id not in self.loans[reader_id]:
            raise ValueError("Эта книга не числится за читателем")
        self.loans[reader_id].remove(book_id)
        self.books[book_id]["available"] += 1
