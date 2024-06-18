import math

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

class color:
    def invert():
        return "\033[7m"
    
    def reset():
        return "\033[0m"

class label(element):
    def __init__(self, size = 1, content = "example") -> None:
        super().__init__(size, False)
        self.content = content

    def process(self, indent=0, space=255):
        self.render = (" " * indent + self.content + "\n")
        
class slider(element):
    def __init__(self, width=10, value=1, max=10) -> None:
        super().__init__(1, True)
        self.width = width
        self.value = value
        self.max = max
        
    def process(self, indent=0, space=255):
        step_size = self.max / self.width
        scaled_val = self.value / step_size
        
        progress_bar = "["
        progress_bar += "#" * math.floor(scaled_val)
        progress_bar += "-" * (self.width - math.floor(scaled_val))
        progress_bar += "] "
        
        progress_percent = str(int(self.value / self.max * 100)) + "%"
        
        self.render = (" " * indent + progress_bar + progress_percent + "\n")

class statusdisplay(label):
    def __init__(self, size=1, content="example", callback=None) -> None:
        super().__init__(size, content)
        self.callback = callback
    
    def process(self, indent=0, space=255):
        return super().process(indent, space) + self.callback()
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
