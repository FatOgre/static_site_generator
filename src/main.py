from textnode import *

def main():
    text_node_one = TextNode("Hello world", TextType.BOLD, "www.github.com")
    text_node_two = TextNode("Zdravo svet!", TextType.ITALIC, "www.24ur.com")

    print(text_node_one)
    print(text_node_two)

main()