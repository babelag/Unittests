import unittest
from first_project import avg

class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1,2,3,4,5,6,7), 4)
        pass

    def test_easy_input_two(self):
        self.assertEqual(avg(10,10,10,10,10), 10)
        pass



class MediumTestCase(unittest.TestCase):

    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, "Hubert"), 4)


    def test_medium_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, "100"), 4)

class HardTestCase(unittest.TestCase):

    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, None), 4)

    def test_hard_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, float), 4)

    def test_hard_input_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, set), 4)

    def test_hard_input_four(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, 4, 5, 6, 7, frozenset), 4)

if __name__ == '__main__':
    unittest.main()