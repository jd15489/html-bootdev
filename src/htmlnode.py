

class HTMLNode:
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: HTMLNode = None,
                 props: {str : str} = None,
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"tag={self.tag},\nvalue={self.value},\nchildren={self.children},\nprops={self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == '':
            return ''
        else:
            return ''.join([f' {k}="{v}"' for k,v in self.props.items()])

class LeafNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 value: str,
                 props: {str : str} = None,
                ):
        super().__init__(tag = tag,
                         value = value,
                         props = props,
                        )

    def to_html(self):
        if self.value == '' or self.value is None:
            raise ValueError('Must have a value')
        elif self.tag == '' or self.tag is None:
            return self.value
        else:
            if self.props is None:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 children: HTMLNode,
                 props: {str : str} = None
                ):
        super().__init__(tag = tag,
                         children = children,
                         props = props,
                        )
    
    def to_html(self):
        if self.tag == '' or self.tag is None:
            raise ValueError('Needs a tag')
        elif self.children is None:
            raise ValueError('Must have children')
        else:
            string = f'<{self.tag}>'
            for child in self.children:
                string += child.to_html()
            string += f'</{self.tag}>'
            return string
