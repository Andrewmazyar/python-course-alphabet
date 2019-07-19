import unittest
import random


def create_list_with_random_numbers():
    return [random.randint(0, 100) for _ in range(20)]


"""
1. число елементів в списку
2. чи кожен елемент цього списку являється інтом
3. чи кожен елемент цього списку знаходиться в заданому діапазоні
4. чи повертає функція саме СПИСОК
"""


class TestCreateListWithRandomNumbers(unittest.TestCase):

    def test_length_of_list(self):

        actual_result = create_list_with_random_numbers()
        self.assertTrue(actual_result)
        self.assertEqual(len(actual_result), 20)

    def test_value_type(self):
        actual_result = create_list_with_random_numbers()
        self.assertTrue(actual_result)
        for i in actual_result:
            self.assertIsInstance(i, int)

    def test_item_value_in_range(self):
        actual_result = create_list_with_random_numbers()
        self.assertTrue(actual_result)
        for i in actual_result:
            self.assertTrue(0 < i <= 100)

    def test_list_returned(self):
        actual_result = create_list_with_random_numbers()
        self.assertTrue(actual_result)
        self.assertIsInstance(actual_result, list)


if __name__ == 'main':
    unittest.main()