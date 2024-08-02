import unittest
from src.utils import load_nodes

class TestUtils(unittest.TestCase):
    def test_load_nodes(self):
        nodes = load_nodes('data/nodes.json')
        self.assertIn("start", nodes)
        self.assertIn("left", nodes)
        self.assertIn("right", nodes)

if __name__ == '__main__':
    unittest.main()
