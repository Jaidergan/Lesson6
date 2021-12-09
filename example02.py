"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def func(self, weight, depth):
        print(self.length * self.width * weight * depth / 1000, "ton", sep=" ")


road = Road(20, 5000)
weight_user = int(input("Масса: "))
depth_user = int(input("Толщина: "))
road.func(weight_user, depth_user)
