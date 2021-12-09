"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import randrange


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print("Машина поехала.")

    def car_stop(self):
        print("Машина остановилась.")

    def car_turn_right(self):
        print("Машина повернула направо")

    def car_turn_left(self):
        print("Машина повернула налево.")

    def car_show_speed(self):
        print(f"Скорость машины: {self.speed}")


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("Это городской автомобиль.")
        print(f"Скорость машины: {self.speed}")
        if self.speed > 60:
            print("Скорость автомобиля превышает предельную скорость.")


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("Это рабочая машина.")
        print(f"Скорость машины: {self.speed}")
        if self.speed > 40:
            print("Скорость автомобиля превышает предельную скорость.")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(randrange(30, 100), "grey", "Ford", False)
car_1.car_show_speed()
print("Цвет: ", car_1.color)
print("Имя: ", car_1.name)
print()
car_2 = WorkCar(randrange(30, 100), "green", "Mercedes", False)
car_2.car_show_speed()
print("Цвет: ", car_2.color)
print("Имя: ", car_2.name)
print()
car_3 = SportCar(randrange(30, 100), "red", "Lamborghini", False)
print("Это спортивный автомобиль.")
car_3.car_show_speed()
print("Цвет: ", car_3.color)
print("Имя: ", car_3.name)
print()
car_4 = PoliceCar(randrange(30, 100), "blue", "Toyota", True)
print("Это полицейская машина.")
car_4.car_show_speed()
print("Цвет: ", car_4.color)
print("Имя: ", car_4.name)
