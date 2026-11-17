class CargoItem:
    def __init__(self, tracking_id, weight):
        self.tracking_id = tracking_id
        self.__weight = weight

    # * Метод __str__ срабатывает автоматически, когда вы делаете print(объект)
    def __str__(self):
        return f"Груз [{self.tracking_id}] | Вес: {self.__weight} кг"

    def get_weight(self):
        return self.__weight

    def update_weight(self, new_weight):
        if new_weight > 0:
            self.__weight = new_weight
        else:
            print("Ошибка: Вес груза не может быть отрицательным!")


# * Создаем груз
box = CargoItem("TRK-987", 500)

# * Теперь эта команда выдаст красивый текст, а не адрес в памяти
