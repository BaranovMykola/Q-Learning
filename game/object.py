class object:

    def __init__(self, name, reward, end=False, color=(0,0,0)):
        self.name = name
        self.reward = reward
        self.color = color
        self.end = end


    def __eq__(self, other):
        return self.name == other.name and\
               self.reward == other.reward and\
               self.color == other.color and\
               self.end == other.end