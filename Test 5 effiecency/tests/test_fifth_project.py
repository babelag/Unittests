import time
import unittest
from fifth_project import FibonacciSequence

class TestEffiecency(unittest.TestCase):

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._effiecency_data = dict()

    def test_first_method(self):
        starting_time = time.time()

        self._fibonacci_sequence.recursive_method(35)

        ending_time = time.time()

        self._effiecency_data['recursive_method'] = ending_time - starting_time

        print(self._effiecency_data)

    def test_second_method(self):
        starting_time = time.time()

        self._fibonacci_sequence.math_method(35)

        ending_time = time.time()

        self._effiecency_data['math_method'] = ending_time - starting_time

        print(self._effiecency_data)

    def tearDown(self):
        self._fibonacci_sequence = None
        self._effiecency_data.clear()
        print(self._effiecency_data)

if __name__ == '__main__':
    unittest.main()