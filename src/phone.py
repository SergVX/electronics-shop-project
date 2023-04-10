from src.item import Item


class Phone(Item):
    """Клас телефоны"""

    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = sim_count

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count):
        if isinstance(count, int) and count > 0:
            self.__number_of_sim = count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"