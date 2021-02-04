
class Flag:
    width : int
    height : int
    name : str

    def __init__(self,width,height,name='UnKnown'):
        self.width = width
        self.height = height
        self.name = name
        assert width >= height
    
    def draw(self):
        raise NotImplementedError()


class AmericaFlag(Flag):
    pass



