import unittest
from exercise_1 import Car


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 20)


    def test_easy_input_two(self):
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        with self.assertRaises(Exception):
            self.car.start_car()


    def test_medium_input_two(self):
        # Todo: use the object car to remove speed 4 times.
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None



class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(),0)

    def test_hard_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        # Todo: use the object car to add speed 2 times.
        self.car.stop()
        self.car.stop()
        self.car.stop()
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: stop the car.
        self.assertEqual(self.car.current_speed(), 0)
        # Todo: make sure that the current speed is 0.
        pass

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()