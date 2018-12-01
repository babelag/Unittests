import unittest
import sys
from io import StringIO
from challenge4 import Printer

class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.printer = Printer()
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_easy_input1(self):
        self.printer.set_value("Hubert")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Hubert')

    def test_easy_input2(self):
        self.printer.set_value("Krzysztof")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Krzysztof')


    def tearDown(self):
        self.printer = None



if __name__ == '__main__':
    unittest.main()