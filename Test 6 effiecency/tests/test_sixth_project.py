import unittest
import time
from sixth_project import AddingMethod

class TestAdding(unittest.TestCase):

    def setUp(self):
        self._adding_method = AddingMethod()
        self._adding_data = dict()

    def test_first_method(self):
        starting_time = time.time()
        self._adding_method.addin_two_first_method(10000000)
        ending_time = time.time()
        self._adding_data['first_method'] = ending_time - starting_time


    def test_second_method(self):
        starting_time = time.time()
        self._adding_method.adding_two_second_method(1000000)
        ending_time = time.time()
        self._adding_data['second_method'] = ending_time - starting_time

    def tearDown(self):
        print(self._adding_data)
        self._adding_method = None


if __name__ == '__main__':
    unittest.main()






