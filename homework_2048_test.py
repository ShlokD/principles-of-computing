import unittest
from homework_2048 import merge

class MyTestCase(unittest.TestCase):
    def test_merge_1(self):
        actual = merge([2, 0, 2, 4])
        expected = [4, 4, 0, 0]
        self.assertEqual(actual, expected)

    def test_merge_2(self):
        actual = merge([0, 0, 2, 2])
        expected = [4, 0, 0, 0]
        self.assertEqual(actual, expected)


    def test_merge_3(self):
        actual = merge([2, 2, 0, 0])
        expected = [4, 0, 0, 0]
        self.assertEqual(actual, expected)


    def test_merge_4(self):
        actual = merge([2, 2, 2, 2, 2])
        expected = [4, 4, 2, 0, 0]
        self.assertEqual(actual, expected)

    def test_merge_5(self):
        actual = merge([8, 16, 16, 8])
        expected = [8, 32, 8, 0]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
