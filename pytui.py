class element:
    def __init__(self,size=1,selectable=False) -> None:
        self.size = size
        self.selectable = selectable
        self.render = ""
        pass
    def process(self, indent = 0, space = 255):
        self.render = ""
    def draw(self):
        return self.render


class label(element):
    def __init__(self, size = 1, content = "example") -> None:
        super().__init__(size, False)
        self.content = content

    def process(self, indent=0, space=255):
        self.render = (" " * indent + self.content + "\n")
        
class slider(element):
    def __init__(self) -> None:
        super().__init__(1,True)

class init():
    def __init__(self) -> None:
        self.elements=[]
        pass
    def addElemement(self,element):
        self.elements.append(element)
    def draw(self):
        for element in self.elements:
            element.process()
        line = 0
        print("\033c", end="")
        for element in self.elements:
            print(element.draw(), end="")
            line += element.size