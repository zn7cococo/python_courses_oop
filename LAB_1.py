import doctest

class Chair:
    """
        Документация на класс.
        Класс описывает модель стула.
    """

    def __init__(self, legs_quantity: int, seat_square: float):
        """
         Создание и подготовка к работе объекта Стул.
         :param legs_quantity: количество ног стула
         :param seat_square: площадь сиденья
         Примеры:
         >>> chair = Chair(4, 0.16)  # инициализация экземпляра класса
         """

        if not isinstance(legs_quantity, int):
            raise TypeError("Количество ножек стула должно быть типа int")
        if legs_quantity <= 0:
            raise ValueError("Количество ножек стула должно быть положительным числом")
        self.legs_quantity = legs_quantity

        if not isinstance(seat_square, float):
            raise TypeError("Площадь сидения стула должена быть float")
        if seat_square <= 0:
            raise ValueError("Площадь сидения стула должена быть положительным числом")
        self.seat_square = seat_square

    def is_childish(self) -> bool:
        """
                Функция которая позволяет вычислить детский ли стул
                :return: Является ли стул детским
                Примеры:
                >>> glass = Chair(3, 0.1)
                >>> glass.is_childish()
        """
        ...

    def count_quantity_of_people(self, body_size: float) -> int:
        """
            Функция, которая позволяет вычислить сколько людей поместиться на стуле
            :return: Объем стакана
            Примеры:
            >>> glass = Chair(3, 0.1)
            >>> glass.count_quantity_of_people(0.05)
        """
        ...

class Box:
    """
        Документация на класс.
        Класс описывает модель коробки.
    """

    def __init__(self, edge: float, foam_rubber: float):
        """
         Создание и подготовка к работе объекта Коробка.
         :param edge: ребро коробки
         :param foam_rubber: количество поролона внутри
         Примеры:
         >>> box = Box(50.0,10.0)  # инициализация экземпляра класса
         """

        if not isinstance(edge, float):
            raise TypeError("Ребро коробки должно быть типа float")
        if edge <= 0:
            raise ValueError("Ребро коробки должно быть быть положительным числом")
        self.edge = edge

        if not isinstance(foam_rubber, float):
            raise TypeError("Объем поролона внутри должно быть типа float")
        if foam_rubber <= 0:
            raise ValueError("Объем попролона внутри быть быть положительным числом")
        self.foam_rubber = foam_rubber

    def count_volume(self) -> float:
        """
                Функция которая позволяет вычислить объем коробки
                :return: Объем коробки
                Примеры:
                >>> box = Box(30.0, 10.0)
                >>> box.count_volume()
        """
        ...

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой
        :return: Является ли коробка пустой
        Примеры:
        >>> box = Box(30.0, 10.0)
        >>> box.is_empty_box()
        """
        ...

class Flat:
    """
        Документация на класс.
        Класс описывает модель квартиры.
    """

    def __init__(self, rooms: int, toilets: int):
        """
         Создание и подготовка к работе объекта Квартира.
         :param floor: количество комнат в квартире
         :param toilets: количество туалетов в квартире
         Примеры:
         >>> flat = Flat(3,1)  # инициализация экземпляра класса
         """

        if not isinstance(rooms, int):
            raise TypeError("Количество комнат в квартире должно быть типа int")
        if rooms <= 0:
            raise ValueError("Количество комнат в квартире должно быть быть положительным числом")
        self.rooms = rooms

        if not isinstance(toilets, int):
            raise TypeError("количество туалетов в квартире должно быть типа int")
        if toilets <= 0:
            raise ValueError("количество туалетов в квартире должно быть быть положительным числом")
        self.toilets = toilets

    def count_prise(self) -> float:
        """
                Функция которая позволяет вычислить сколько стоит квартира
                :return: Цена квартиры
                Примеры:
                >>> flat = Flat(3,1)
                >>> flat.count_prise()
        """
        ...

    def are_there_toilets(self) -> bool:
        """
        Функция которая проверяет есть ли в квартире туалеты
        :return: Есть ли в квартире туалеты
        Примеры:
        >>> flat = Flat(3,1)
        >>> flat.are_there_toilets()
        """
        ...




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()