import unittest
from unique import Unique

class TestUnique(unittest.TestCase):

    def test_empty_sequence(self):
        unique_iter = Unique([])
        with self.assertRaises(StopIteration):
            next(unique_iter)

    def test_unique_sequence(self):
        unique_iter = Unique([1, 2, 3, 4, 5])
        self.assertEqual([next(unique_iter) for _ in range(5)], [1, 2, 3, 4, 5])
        with self.assertRaises(StopIteration):
            next(unique_iter)

    def test_duplicate_sequence(self):
        unique_iter = Unique([1, 2, 2, 3, 3, 3, 1, 4])
        self.assertEqual([next(unique_iter) for _ in range(4)], [1, 2, 3, 4])
        with self.assertRaises(StopIteration):
            next(unique_iter)

    def test_ignore_case(self):
        unique_iter = Unique(['a', 'A', 'b', 'B', 'c'], ignore_case=True)
        self.assertEqual([next(unique_iter) for _ in range(3)], ['a', 'b', 'c'])
        with self.assertRaises(StopIteration):
            next(unique_iter)

    def test_mixed_types(self):
        unique_iter = Unique([1, 'a', 1, 'A', 'b', 2])
        self.assertEqual([next(unique_iter) for _ in range(5)], [1, 'a', 'A', 'b', 2])


    def test_ignore_case_mixed_types(self):
        unique_iter = Unique([1, 'a', 1, 'A', 'b', 2], ignore_case=True)
        self.assertEqual([next(unique_iter) for _ in range(4)], [1, 'a', 'b', 2])


if __name__ == '__main__':
    unittest.main()

