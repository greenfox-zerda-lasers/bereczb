import unittest
import a01
import a02
import a03


class Week5_Day3_a01_TestCase(unittest.TestCase):
    def test_divide_zerodivisionerror(self):
        self.assertEqual(a01.divide(0), 'fail')

class Week5_Day3_b02_TestCase(unittest.TestCase):
    def test_number_of_lines_filenotfounderror(self):
        self.assertEqual(a02.number_of_lines('a01py'), 0)

class Week5_Day3_b03_TestCase(unittest.TestCase):
    def test_birth_date_valueerror(self):
        self.assertRaises(ValueError, a03.Person, 'a', -1)
        self.assertEqual(a03.Person('lalala', 1999).name, 'lalala')

if __name__ == '__main__':
    unittest.main()
