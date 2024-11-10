import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_two(self):
        node = TextNode("This is test node 2", TextType.ITALIC, "www.24ur.com")
        node2 = TextNode("This is test node 2", TextType.ITALIC, "www.24ur.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is test node 2", TextType.BOLD)
        node2 = TextNode("This is test node 2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_two(self):
        node = TextNode("This is test node 2", TextType.BOLD, "www.24ur.com")
        node2 = TextNode("This is test node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_three(self):
        node = TextNode("This is test node", TextType.ITALIC)
        node2 = TextNode("This is test node 2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()