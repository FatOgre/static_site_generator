class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        return props_to_str(self.props)
    
    def __repr__(self) -> str:
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, props = props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None or not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {props_to_str(self.props)}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Value error: No tag!")
        if self.children is None or not self.children:
            raise ValueError("Value error: No children!")
        html_string = ""
        for node in self.children:
            html_string += node.to_html()

        return f"<{self.tag}>{html_string}</{self.tag}>"

        
    
def props_to_str(prop_dict: dict):
    if prop_dict is None:
        return ""

    prop_list = []
    for key, value in prop_dict.items():
        prop_list.append(f'{key}="{value}"')
    return " ".join(prop_list)
