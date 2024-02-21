import unittest
from tree_app import generate_tree, validate_levels

class TestTree(unittest.TestCase):

    def test_generate_tree_structure(self):
        levels_test_cases = [5, 10, 100]
        for levels in levels_test_cases:
            with self.subTest(levels=levels):
                tree = generate_tree(levels)
                self.assertIsInstance(tree, str)
                self.assertGreater(len(tree), 0)
                self.assertIn('W', tree)
                self.assertIn('*', tree)
                self.assertIn('TTTTT', tree)

    def test_validate_levels(self):
        valid_levels = [3, 4, 999, 1000]
        invalid_levels = ['a', 2, 1001, -10, 0]

        for level in valid_levels:
            with self.subTest(level=level):
                self.assertEqual(validate_levels(level), level)

        for level in invalid_levels:
            with self.subTest(level=level):
                with self.assertRaises(ValueError):
                    validate_levels(level)



if __name__ == '__main__':
    unittest.main()
