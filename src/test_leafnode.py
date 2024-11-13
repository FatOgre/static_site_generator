import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_test_one(self):
        leaf_node_one = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node_one.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_node_test_two(self):
        leaf_node_one = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node_one.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_three(self):
        leaf_node = LeafNode("a", "Click me!", {})
        self.assertEqual(leaf_node.to_html(), '<a>Click me!</a>')

    def test_leaf_node_four(self):
        leaf_node = LeafNode(None, "Click me!")
        self.assertEqual(leaf_node.to_html(), 'Click me!')

if __name__ == "__main__":
    unittest.main()