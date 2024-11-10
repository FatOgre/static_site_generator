import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_prop_to_html_one(self):
        prop_one = {
            "href": "https://www.google.com", 
            "target": "_blank",
            "style": "css"
        }
        html_one = HTMLNode(props = prop_one)
        self.assertEqual(html_one.props_to_html(), 'href="https://www.google.com" target="_blank" style="css"')

    def test_prop_to_html_two(self):
        prop_two = {
            "href": "https://www.google.com", 
            "color": "black"
        }
        html_two = HTMLNode(props = prop_two)
        self.assertEqual(html_two.props_to_html(), 'href="https://www.google.com" color="black"')

    def test_to_prop_three(self):
        prop_three = {
            "href": "www.24ur.com", 
        }
        html_three = HTMLNode(props = prop_three)
        self.assertEqual(html_three.props_to_html(), 'href="www.24ur.com"')

    def test_to_prop_four(self):
        html_four = HTMLNode()
        self.assertEqual(html_four.props_to_html(), '')

    
    
    

    