import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) ->None:
        self.calculator =Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.square_root(4), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_add_csv(self):
        test_data_add = CsvReader("../src/CsvFiles/Unit Test Addition.csv").data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_csv(self):
        test_data_subtract = CsvReader("../src/CsvFiles/Unit Test Subtraction.csv").data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    if __name__ == '__main__':
        unittest.main()