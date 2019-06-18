from objects_and_classes.homework.homework import (
    Car,
    Garage,
    Cesar,
    )
import unittest


class CesarTest(unittest.TestCase):

    def test_add_garage(self):
        cesar = Cesar('Alfred')
        garage_1 = Garage(6)
        cesar.add_garage(garage_1)
        self.assertEqual(len(cesar.garages), 1)

    def test_add_car(self):
        cesar = Cesar('Alfred')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        garage_3 = Garage(8)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        cesar.add_garage(garage_3)
        cesar.add_car(car_1, garage_1)  # add car with specific garage
        cesar.add_car(car_2)  # add car without specific garage
        self.assertEqual(garage_1.free_place(), 3)  # check our method
        self.assertEqual(garage_3.free_place(), 7)  # check our method

    def test_garages_count(self):
        cesar = Cesar('Alfred')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        garage_3 = Garage(8)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        cesar.add_garage(garage_3)
        self.assertEqual(cesar.garages_count(), 3)

    def test_cars_count(self):
        cesar = Cesar('Alfred')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        garage_3 = Garage(8)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)
        car_3 = Car(3000, 500)
        car_4 = Car(300, 50)
        car_5 = Car(300000, 50000)
        car_6 = Car(3000000, 500000)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        cesar.add_garage(garage_3)
        cesar.add_car(car_1, garage_1)
        cesar.add_car(car_2, garage_1)
        cesar.add_car(car_3, garage_2)
        cesar.add_car(car_4, garage_2)
        cesar.add_car(car_5, garage_3)
        cesar.add_car(car_6, garage_3)
        self.assertEqual(cesar.cars_count(), 6)

    def test_hit_hat(self):
        cesar = Cesar('Alfred')
        garage_1 = Garage(4)
        garage_2 = Garage(2)
        garage_3 = Garage(8)
        car_1 = Car(25000, 10000)
        car_2 = Car(30000, 5000)
        car_3 = Car(3000, 500)
        car_4 = Car(300, 50)
        car_5 = Car(300000, 50000)
        car_6 = Car(3000000, 500000)
        cesar.add_garage(garage_1)
        cesar.add_garage(garage_2)
        cesar.add_garage(garage_3)
        cesar.add_car(car_1, garage_1)
        cesar.add_car(car_2, garage_1)
        cesar.add_car(car_3, garage_2)
        cesar.add_car(car_4, garage_2)
        cesar.add_car(car_5, garage_3)
        cesar.add_car(car_6, garage_3)
        self.assertEqual(cesar.hit_hat(), 3358300)

    def test_equal(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(100, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_not_equal(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(1000, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertNotEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_less_equal(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(10, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertLessEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_more_equal(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(1000, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertGreaterEqual(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_more_than(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(1000, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertGreater(cesar_1.hit_hat(), cesar_2.hit_hat())

    def test_less_than(self):
        cesar_1 = Cesar('Alfred')
        cesar_2 = Cesar('Hector')
        garage_1 = Garage(2)
        garage_2 = Garage(2)
        garage_3 = Garage(2)
        garage_4 = Garage(2)
        car_1 = Car(10, 10000)
        car_2 = Car(100, 5000)
        car_3 = Car(100, 500)
        car_4 = Car(100, 50)
        car_5 = Car(100, 50000)
        car_6 = Car(100, 500000)
        cesar_1.add_garage(garage_1)
        cesar_1.add_garage(garage_2)
        cesar_2.add_garage(garage_3)
        cesar_2.add_garage(garage_4)
        cesar_1.add_car(car_1, garage_1)
        cesar_1.add_car(car_2, garage_2)
        cesar_1.add_car(car_3, garage_2)
        cesar_2.add_car(car_4, garage_3)
        cesar_2.add_car(car_5, garage_4)
        cesar_2.add_car(car_6, garage_4)
        self.assertLess(cesar_1.hit_hat(), cesar_2.hit_hat())


class GarageTest(unittest.TestCase):
    def test_free_place(self):
        garage = Garage(7)
        car = Car(10, 100)
        garage.add_car(car)
        self.assertEqual(garage.free_place(), 6)

    def test_add_car(self):
        garage = Garage(2)
        car_1 = Car(10, 10)
        car_2 = Car(11, 11)
        car_3 = Car(12, 12)
        garage.add_car(car_1)
        garage.add_car(car_2)
        self.assertEqual(garage.free_place(), 0)
        self.assertEqual(garage.add_car(car_3), "you do not have enough space in garage")

    def test_remove_car(self):
        garage = Garage(3)
        car_1 = Car(10, 10)
        car_2 = Car(11, 11)
        car_3 = Car(12, 12)
        garage.add_car(car_1)
        garage.add_car(car_2)
        garage.add_car(car_3)
        garage.remove(car_3)
        self.assertEqual(garage.free_place(), 1)

    def test_hit_hat(self):
        garage = Garage(3)
        car_1 = Car(110, 10)
        car_2 = Car(110, 11)
        car_3 = Car(110, 12)
        garage.add_car(car_1)
        garage.add_car(car_2)
        garage.add_car(car_3)
        self.assertEqual(garage.hit_hat(), 330)


class CarTest(unittest.TestCase):
    def test_change_number(self):
        car = Car(100, 1000)
        self.assertNotEqual(car.number, car.change_number())

    def test_less_than(self):
        car_1 = Car(100, 100)
        car_2 = Car(101, 100)
        self.assertLess(car_1.price, car_2.price)

    def test_more_than(self):
        car_1 = Car(1000, 100)
        car_2 = Car(100, 100)
        self.assertGreater(car_1.price, car_2.price)

    def test_more_equal(self):
        car_1 = Car(1000, 100)
        car_2 = Car(100, 100)
        self.assertGreaterEqual(car_1.price, car_2.price)

    def test_less_equal(self):
        car_1 = Car(100, 100)
        car_2 = Car(101, 100)
        self.assertLessEqual(car_1.price, car_2.price)

    def test_not_equal(self):
        car_1 = Car(100, 100)
        car_2 = Car(101, 100)
        self.assertNotEqual(car_1.price, car_2.price)

    def test_equal(self):
        car_1 = Car(100, 100)
        car_2 = Car(100, 100)
        self.assertEqual(car_1.price, car_2.price)


if __name__ == '__main__':
    unittest.main()