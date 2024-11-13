import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_one(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Click me!</a></p>')

    def test_parent_node_two(self):
        node = ParentNode(
            "p",
            [
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_three(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p", [
                    LeafNode("i", "italic text in another parent"),
                ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b><p><i>italic text in another parent</i></p>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Click me!</a></p>')

    def test_parent_node_four(self):
        node = ParentNode(
            "p",
            [
                ParentNode("pa", [
                    LeafNode("i", "italic text in another parent"),
                ]),
            ],
        )
        self.assertEqual(node.to_html(), '<p><pa><i>italic text in another parent</i></pa></p>')

    def test_parent_node_five(self):
        node = ParentNode(
            "p",
            [
                ParentNode(None, [
                    LeafNode("i", "italic text in another parent"),
                ]),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_six(self):
        node = ParentNode(
            "p",
            [
                ParentNode("pa", [
                    LeafNode("i"),
                ]),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_seven(self):
        node = ParentNode(
            "p",
            [
                ParentNode("pa", [
                    ParentNode("pa2", [
                        LeafNode("i", "italic text in another parent"),
                        LeafNode(None, "Normal text"),
                    ]),
                ]),
            ],
        )
        self.assertEqual(node.to_html(), '<p><pa><pa2><i>italic text in another parent</i>Normal text</pa2></pa></p>')

if __name__ == '__main__':
    unittest.main()