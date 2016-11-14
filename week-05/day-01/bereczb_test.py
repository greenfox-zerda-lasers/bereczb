import unittest
import bereczb_work

class AnagrammTestCase(unittest.TestCase):

    def test_anagramm_true(self):
        self.assertTrue(bereczb_work.anagramm('szabad lexikon', 'Indexkaszabol'))

    def test_anagramm_false(self):
        self.assertFalse(bereczb_work.anagramm('szabad lexikon', 'Indexkaszabo'))

    def test_anagramm_typeerror(self):
        self.assertRaises(TypeError, bereczb_work.anagramm, 1, 'Indexkaszabo')

    def test_count_letters_equal(self):
        self.assertEqual(bereczb_work.count_letters('abc!!!  aaaa bb----cccc'), {'a': 5, 'b': 3, 'c': 5})

    def test_count_letters_dictionary(self):
        self.assertIsInstance(bereczb_work.count_letters('abc!!!  aaaa bb----cccc'), dict)

if __name__ == '__main__':
    unittest.main()
