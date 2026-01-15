from enum import Enum

class TextType(Enum):
    TEXT = 'text (plain)'
    BOLD = '**Bold text**'
    ITALIC = '_Italic text'
    CODE = '`Code text`'
    LINK = '[anchor text](url)'
    IMAGE = '![alt text](url)'

class TextNode:
    def __init__(self,
                 text: str,
                 text_type: TextType,
                 url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url or self.url is None and other.url is None:
                    return True
        #All Else
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.name}, {self.url})'
