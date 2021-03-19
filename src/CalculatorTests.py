import unittest
from Calculator import Calculator
# from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Calculator, Calculator)




if __name__ == '__main__':
    unittest.main()