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
    remove(car) -> Забирає машину з гаражу.
    remove(cat) -> Забирає машину з гаражу.
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

    def add_garage(self, garage):
        self.garages.append(garage)
        garage.owner = self.name

    def hit_hat(self):
        sum = 0
        for car in self.garages:
            sum += car.hit_hat()
        return sum

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def garages_count(self):
        return len(self.garages)

    def add_car(self, car, garage=None):
        if garage:
            if garage in self.garages:
                garage.add_car(car)
        else:
            place_list = []
            for garage in self.garages:
                place_list.append(garage.free_place())
            for garage in self.garages:
                if garage.free_place() == max(place_list):
                    garage.add_car(car)

    def cars_count(self):
        sum_car = 0
        for car in self.garages:
            sum_car += len(car.cars)
        return sum_car


class Car:
    def __init__(self, price, mileage):
        self.price = price
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.number = uuid.uuid4()
        self.mileage = float(mileage)

    def __repr__(self):
        return f"price car: {self.price},\ntype: {self.type},\nnumber: {self.number}, \nmileage: {self.mileage}," \
            f"producer: {self.producer}"

    def __ne__(self, other):
        return self.price != other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def change_number(self):
        self.number = uuid.uuid4()
        return self.number


class Garage:
    def __init__(self, places):
        self.town = random.choice(TOWNS)
        self.cars = []
        self.places = places
        self.owner = Cesar.register_id

    def free_place(self):
        return self.places - len(self.cars)

    def add_car(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return self.cars
        else:
            return "you do not have enough space in garage"

    def remove(self, car):
        self.cars.remove(car)

    def hit_hat(self):
        sum = 0
        for price in self.cars:
            sum += price.price
        return sum