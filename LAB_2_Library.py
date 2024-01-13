BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id: int, name: str, pages: int):

        if not isinstance(id, int):
            raise TypeError("Индентификатор книги должен быть типа int")
        if id <= 0:
            raise ValueError("Индентификатор книги должен быть положительным числом")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'

class Library:

    def __init__(self, books: list = []):

        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, id_serch) -> int:
        index = [self.books.index(book) for book in self.books if book.id == id_serch]
        return index[0]


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
