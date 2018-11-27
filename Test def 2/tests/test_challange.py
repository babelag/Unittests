import unittest
from challange import counter

class EasyTestCase(unittest.TestCase):

    def test_first_input(self):
        self.assertEqual(counter('Hubert'), 6)

    def test_second_input(self):
        self.assertEqual(counter('Dagmara'), 7)


class MediumTestCase(unittest.TestCase):

    def test_first_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter('Hub#@!'), 3)

    def test_second_input(self):
        self.assertEqual(counter('Hubert Hubert'), 12)

class HardTestCase(unittest.TestCase):

    def test_first_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter(''), 0)

    def test_second_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter(None), 0)


if __name__ == '__main__':
    unittest.main()