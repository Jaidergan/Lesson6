"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("!!!Запуск отрисовки!!!")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"{self.title} пишет в тетрадке.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"{self.title} рисует на листке.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"{self.title} выводит на доске.")


draw_1 = Pen("Ручка")
draw_1.draw()
draw_2 = Pencil("Карандаш")
draw_2.draw()
draw_3 = Handle("Маркер")
draw_3.draw()
