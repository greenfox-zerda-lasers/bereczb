import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_4_and_3_is_7(self):
        self.assertEqual(extend.add(4, 3), 7)

    def test_add_4_and_2_is_(self):
        self.assertEqual(extend.add(4, 2), 6)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(4, 3, 5), 5)

    def test_median_four(self):
        self.assertEqual(extend.median([4,1,3,2]), 2.5)

    def test_median_five(self):
        self.assertEqual(extend.median([3,2,1,4,5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbico'), 'kovolbivicovo')

if __name__ == '__main__':
    unittest.main()
