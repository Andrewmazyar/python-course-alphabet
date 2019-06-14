"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
<<<<<<< HEAD
    remove(car) -> Забирає машину з гаражу.
=======
    remove(cat) -> Забирає машину з гаражу.
>>>>>>> 5b8510124724f43e3dd24ecbe8263bf5e3300e86
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
<<<<<<< HEAD
from objects_and_classes.homework.constants import (
    CARS_PRODUCER,
    CARS_TYPES,
    TOWNS
)
import uuid
import random


class Cesar:
    register_id = None

    def __init__(self, name):
        self.name = name
        self.garages = []
        self.register_id = uuid.uuid4()
        self.garage = Garage()
        if self.register_id == self.garage.owner:
            self.garages.append(self.garage)

    def hit_hat(self):
        self.sum = 0
        for car in self.garages:
            self.sum += car.hit_hat()
        return self.sum

    def comparison_cesar(self, other):
        if self.hit_hat() == other.hit_hat():
            return f"this Cesar {self.name} is the same Cesar {other.name}"
        elif self.hit_hat() < other.hit_hat():
            return f"this Cesar {self.name} is more cheaper with this Cesar {other.name}"
        elif self.hit_hat() > other.price():
            return f"this Cesar {self.name} is more expensive with this Cesar {other.name}"

    def garages_count(self):
        return len(self.garages)

    def add_car(self, car, garage=None):
        if garage:
            if garage in self.garages:
                garage.add_car(car)
        else:
            place_list = []
            for garage in self.garages:
                place_list.append(garage.free_place)
            for garage in self.garages:
                if garage.free_place == max(place_list):
                    garage.add_car(car)

    def cars_count(self):
        self.sum_car = 0
        for car in self.garages:
            self.sum_car += len(car.cars)
        return self.sum_car


class Car:
    def __init__(self, price, mileage):
        self.price = price
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.number = uuid.uuid4()
        self.mileage = float(mileage)

    def comparison_car(self, other):
        if self.price() == other.price():
            return f"this car {self.price} is the same price with this car {other.car}"
        elif self.price() < other.price():
            return f"this car {self.price} is more cheaper with this car {other.car}"
        elif self.price() > other.price():
            return f"this car {self.price} is more expensive with this car {other.car}"

    def all_info_car(self, item):
        return f"price car: {self.price},\ntype: {self.type},\nnumber: {self.number}, \nmileage: {self.mileage}"

    def change_number(self):
        self.number = uuid.uuid4()
        return self.number


class Garage:
    def __init__(self, places):
        self.town = random.choice(TOWNS)
        self.cars = []
        self.places = places
        self.owner = Cesar.register_id
        self.car = Car()
        self.free_place = self.places - len(self.cars)

    def add_car(self):
        if len(self.cars) < self.places:
            self.cars.append(self.car)
            return f"your car was success add to garage, your car in garage:{self.cars}"
        else:
            return "you do not have enough space in garage, chose another garage"

    def remove(self):
        self.cars.remove(self.car)
        return f"this {self.car} was remove from garage, this list cars in garage: {self.cars}"

    def hit_hat(self):
        self.sum = 0
        for price in self.cars:
            self.sum += self.car[price]
        return self.sum
=======


class Cesar:
    pass


class Car:
    pass


class Garage:
    pass
>>>>>>> 5b8510124724f43e3dd24ecbe8263bf5e3300e86
