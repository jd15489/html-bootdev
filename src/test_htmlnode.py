import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_prop_to_html(self):
        node1 = HTMLNode(props={"href": "https://www.google.com",
                                "target": "_blank",
                               }
                        )
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_prop_to_html_1(self):
        node1 = HTMLNode(tag = 'h1',
                         value = 'text'
                        )
        self.assertEqual(node1.props_to_html(), '')

    def test__repr__(self):
        node1 = HTMLNode(tag = 'h1',
                         value = 'text'
                        )
        self.assertEqual(node1.__repr__(), f'tag=h1,\nvalue=text,\nchildren=None,\nprops=None')

    def test_leafnode(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_1(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    