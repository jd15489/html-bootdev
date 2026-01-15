import unittest

from textnode import TextNode, TextType
from lib import text_node_to_html_node, split_nodes_delimiter

class TestLib(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_plain(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_node_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        nodes_test = [TextNode("This is text with a ", TextType.TEXT),
                      TextNode("code block", TextType.CODE),
                      TextNode(" word", TextType.TEXT),
                     ]
        self.assertEqual(new_nodes, nodes_test)

    def test_split_node_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node1 = TextNode("This is also text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node1], "`", TextType.CODE)
        nodes_test = [TextNode("This is text with a ", TextType.TEXT),
                      TextNode("code block", TextType.CODE),
                      TextNode(" word", TextType.TEXT),
                      TextNode("This is also text with a ", TextType.TEXT),
                      TextNode("code block", TextType.CODE),
                      TextNode(" word", TextType.TEXT),
                     ]
        print(new_nodes)
        self.assertEqual(new_nodes, nodes_test)
