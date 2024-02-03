class Activity:
    """
    Документация на класс.
    Класс описывает модель активности.
    """

    def __init__(self, name: str, author: str, genre: str, age_limit: int, time_taken: int):
        """Инициализация экземпляров класса.

        :param time_taken: количество потраченных на активность минут
        """
        self._name = name
        self._author = author
        self._genre = genre
        self._age_limit = age_limit
        self._time_taken = time_taken

        self.is_valid_data(self._name, self._author, self._genre, self._age_limit,
                           self._time_taken)  # проверка на правильность данных

    # делаем все атрибуты класса защищенными и доступными только для чтения
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    @property
    def age_limit(self):
        return self._age_limit

    @staticmethod
    def is_string(text: list) -> None:
        """Статичный метод опредляющий являеются ли элементы данного списка типа str."""
        for item in text:
            if not isinstance(item, str):
                raise TypeError(f"{item} должен быть типа str")

    @staticmethod
    def is_int(numbers: list) -> None:
        """Статичный метод опредляющий являеются ли элементы данного списка типа int."""
        for item in numbers:
            if not isinstance(item, int):
                raise TypeError(f"{item} должен быть типа int")
            if item < 0:
                raise ValueError(f"{item} должен быть положительным числом")

    @classmethod
    def is_valid_data(cls, name: str, author: str, genre: str, age_limit: int, time_taken: int) -> None:
        """Метод проверяющий соответствие данных нужным типам."""
        cls.is_string([name, author, genre])
        cls.is_int([age_limit, time_taken])

    @staticmethod
    def will_it_fit_my_taste(activity: ('Activity', 'Film', 'Book'), personal_genres: (str, list)) -> bool:
        """Метод определяющий совпадает ли жанр произведения с любимыми жанрами пользователя.

        :param personal_genres: один жанр или их список, введенный пользователем
        """
        if isinstance(personal_genres, str): # проверяем совпадают ли жанры при одном введеном жанре, проверяя его тип
            if personal_genres.upper() == activity._genre.upper(): # используем upper() чтобы данные были идентичны
                return True
            else:
                return False
        elif isinstance(personal_genres, list): # проверяем совпадают ли жанры при введеном списке жанров
            # проходим через каждый элемент массива, выполняя проверку на тип данных и используем upper()
            personal_genres = [item.upper() for item in personal_genres if Activity.is_string(item) is None]
            if activity._genre.upper() in personal_genres: # так же используем upper() для идентичности данных
                return True
            else:
                return False
        else:
            raise TypeError("Список ваших любимых жанров должен быть типа str или list") # в этом методе параллельно
                                                                                         # проверяем типы данных

    def how_much_time_taken(self) -> str:
        """Метод возвращающий количество часов и минут потраченных на активность."""
        return f'Данное занятие займет {self._time_taken // 60} часов и {self._time_taken % 60} минут.'

    def __str__(self) -> str:
        return f'Произведение "{self._name}".'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self._name!r}, ' \
               f'author={self._author!r}, ' \
               f'genre={self._genre!r}, ' \
               f'age_limit={self._age_limit!r}, ' \
               f'time_taken={self._time_taken!r})'


class Film(Activity):
    """
    Документация на класс.
    Класс описывает объект фильма
    """

    # конструктор базового класса наследуем полностью, по этой причине не перегружаем __repr()__

    def __str__(self) -> str:
        return f'Фильм "{self._name}".' # перегружаем __str()__ для удобства пользователя

    # методы will_it_fit_my_taste() и how_much_time_taken() не перегружены так как они должны работать идентично
    # базовому классу

class Book(Activity):
    """
    Документация на класс.
    Класс описывает модель книги.
    """

    def __init__(self, name: str, author: str, genre: str, age_limit: int, pages_number: int, reader_speed: float):
        """
        Инициализируем новый атрибут, наследуя конструктор базового класса.

        :param reader_speed: скорость чтения читателя (страниц в минуту)
        :param pages_number: количество страниц в книге, записивающееся в аргумент time_taken базового класса
        """
        super().__init__(name, author, genre, age_limit, pages_number)
        self._reader_speed = reader_speed

        self.is_float(reader_speed) # проверка атрибута на тип

    @staticmethod # метод описан в дочернем классе, так как не используется в базовом
    def is_float(number: float) -> None:
        """Статичный метод опредляющий являеются ли элементы данного списка типа float."""
        if not isinstance(number, float):
            raise TypeError(f"{number} должен быть типа float")
        if number < 0:
            raise ValueError(f"{number} должен быть положительным числом")

    def how_much_time_taken(self) -> str: # перегружаем метод, так как теперь используем другую формулу для подсчета времени
        return f'Данное занятие займет {int(self._time_taken * self._reader_speed) // 60} часов и {int(self._time_taken * self._reader_speed) % 60} минут.'

    def __str__(self) -> str:
        return f'Книга "{self._name}".' # перегружаем __str()__ для удобства пользователя

    def __repr__(self) -> str: # перегружаем __repr()__ так как был добавлен новый атребут
        return f'{self.__class__.__name__}(name={self._name!r}, ' \
               f'author={self._author!r}, ' \
               f'genre={self._genre!r}, ' \
               f'age_limit={self._age_limit!r}, ' \
               f'time_taken={self._time_taken!r}, ' \
               f'reader_speed={self._reader_speed})'


if __name__ == "__main__":
    activity_1 = Activity("Mamma Mia!", "Phyllida Lloyd", "musical", 16, 108)
    film_1 = Film("Spider-man", "Sam Raimi", "Fantasy", 12, 121)
    book_1 = Book("Var and peace", "Lev Tolstoy", "novEL", 12, 1300, 2.0)
    print(activity_1)
    print(film_1)
    print(book_1)
    print(Activity.will_it_fit_my_taste(activity_1, ["Novel", "Musical"]))
    print(Film.how_much_time_taken(film_1))
    print(Book.how_much_time_taken(book_1))
    pass
