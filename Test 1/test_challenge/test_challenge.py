from challenge import challenge
import unittest

class EasyTestCase(unittest.TestCase):

    def test_easy_input1(self):
        self.assertEqual(challenge.counter('Hubert'), 6 )

    def test_easy_input2(self):
        self.assertEqual(challenge.counter('Translaotr'), 10 )

class MediumTestCase(unittest.TestCase):

    def test_medium_input1(self):
        with self.assertRaises(Exception):
            self.assertEqual(challenge.counter('Tqq@#@!#!@'), 10)

    def test_medium_input2(self):
        self.assertEqual(challenge.counter('Hubert Hubert'), 12 )

class HardTestCase(unittest.TestCase):

    def test_hard_input1(self):
        with self.assertRaises(Exception):
            self.assertEqual(challenge.counter(''), 0 )

    def test_hard_input2(self):
        with self.assertRaises(Exception):
            self.assertEqual(challenge.counter(None), 0 )



if __name__ == '__main__':
    unittest.main()