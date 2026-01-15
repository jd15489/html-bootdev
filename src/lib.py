from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    text = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = None,
                            value=text
                           )
        case TextType.BOLD:
            return LeafNode(tag='b',
                            value = text
                           )
        case TextType.ITALIC:
            return LeafNode(tag = 'i',
                            value = text
                           )
        case TextType.CODE:
            return LeafNode(tag = 'code',
                            value = text
                           )
        case TextType.LINK:
            return LeafNode(tag = 'a',
                            value = text
                           )
        case TextType.IMAGE:
            return LeafNode(tag = 'img',
                            value = '',
                            props = {'src':text_node.url,
                                     'alt':text
                                    }
                           )
        case _: 
            raise TypeError(text_node, text_node.text_type, type(text_node.text_type))

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT and node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            new_type = TextType.TEXT
            for text in split_text:
                if text == '':
                    new_type = text_type
                else:
                    new_nodes.append(TextNode(text,new_type))
                    if new_type == TextType.TEXT:
                        new_type = text_type
                    elif new_type == text_type:
                        new_type = TextType.TEXT
        
    return new_nodes
