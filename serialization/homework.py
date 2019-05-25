"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini
"""
from objects_and_classes.homework.homework import (
    Cesar,
    Garage,
    Car
    )
import json
import ruamel.yaml
from ruamel.yaml import YAML
import pickle


heorh = Cesar('Heorh')
king_garage = Garage(4)
elite_car = Car(500000, 5000)

# ___________convert by JSON____________


def heorh_to_json(obj: Cesar):
    data = {'name': obj.name}
    return data


def king_garage_to_json(obj: Garage):
    data = {'places': obj.places, 'owner': None}
    return data


def elite_car_to_json(obj: Car):
    data = {'price': obj.price, 'mileage': obj.mileage}
    return data

# _________conver from json by string___________


def cesar_from_json(data):
    name = data['name']
    heorh = Cesar(name=name)
    return heorh


def garage_from_json(data):
    places = data['places']
    # owner = data['owner']
    gr = Garage(places=places)
    return gr


def car_from_json(data):
    price = data['price']
    mileage = data['mileage']
    car = Car(price=price, mileage=mileage)
    return car

# _____Convert Cesar, Garage and Car into JSON strings______


encoded_cesar = json.dumps(heorh, default=heorh_to_json)
encoded_garage = json.dumps(king_garage, default=king_garage_to_json)
encoded_car = json.dumps(elite_car, default=elite_car_to_json)


# ______Create Cesar, Garage and Car from json strings_________


decoded_cesar = json.loads(encoded_cesar, object_hook=cesar_from_json)
decoded_garage = json.loads(encoded_garage, object_hook=garage_from_json)
decoded_car = json.loads(encoded_car, object_hook=car_from_json)


# ______Save Cesar, Garage and Car into JSON files_______
with open('heorh.json', 'w') as file:
    json.dump(heorh, file, default=heorh_to_json)

with open('king_garage.json', 'w') as file:
    json.dump(king_garage, file, default=king_garage_to_json)

with open('elite_car.json', 'w') as file:
    json.dump(elite_car, file, default=elite_car_to_json)


# _______Create Cesar, Garage and Car from JSON files______
with open('heorh.json', 'r') as file:
    decoded_cesar = json.load(file, object_hook=cesar_from_json)

with open('king_garage.json', 'r') as file:
    decoded_garage = json.load(file, object_hook=garage_from_json)

with open('elite_car.json', 'r') as file:
    decoded_car = json.load(file, object_hook=car_from_json)

# ___________convert by YAML____________
# _______save Ceser Car and Garage by yaml______


yaml = YAML()
yaml.register_class(Cesar)
with open('heorh.yaml', 'w') as file:
    ruamel.yaml.dump(heorh, file)

yaml.register_class(Garage)
with open('king_garage.yaml', 'w') as file:
    ruamel.yaml.dump(king_garage, file)

yaml.register_class(Car)
with open('elite_car.yaml', 'w') as file:
    ruamel.yaml.dump(elite_car, file)

# ______Create Cesar, Garage and Car from YAML_______

with open('heorh.yaml', 'r') as file:
    heorh = ruamel.yaml.load(file)

with open('king_garage.yaml', 'r') as file:
    king_garage = ruamel.yaml.load(file)

with open('elite_car.yaml', 'r') as file:
    elite_car = ruamel.yaml.load(file)


# ______________PICKLE__________
# Save Cesar, Garage and Car

with open('heorh.txt', 'wb') as file:
    pickle.dump(heorh, file)

with open('king_garage.txt', 'wb') as file:
    pickle.dump(king_garage, file)

with open('elite_car.txt', 'wb') as file:
    pickle.dump(elite_car, file)

# Create Cesar, Garage and Car from Pickle

with open('heorh.txt', 'rb') as file:
    heorh = pickle.load(file)

with open('king_garage.txt', 'rb') as file:
    king_garage = pickle.load(file)

with open('elite_car.txt', 'rb') as file:
    elite_car = pickle.load(file)


# Convert Cesar, Garage and Car into Pickle strings

encoded_cesar = pickle.dumps(heorh)
encoded_garage = pickle.dumps(king_garage)
encoded_car = pickle.dumps(elite_car)

# Create Cesar, Garage and Car from Pickle strings

decoded_cesar = pickle.loads(encoded_cesar)
decoded_garage = pickle.loads(encoded_garage)
decoded_car = pickle.loads(encoded_car)