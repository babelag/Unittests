import unittest
from third_project import Profile
from io import StringIO
import sys

class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile('Hubert', 27, 'Software tester')

    def test_easy_input1(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Hubert')

    def test_easy_input2(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), str(27))

    def test_easy_input3(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Software tester')

    def tearDown(self):
        self.profile = None

if __name__ == '__main__':
    unittest.main()


