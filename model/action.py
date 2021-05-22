class Action:
    def __init__(self, index, type, time, text, position):
        self.index = index
        self.type = type
        self.time = time
        self.text = text
        self.position = position

    def to_cli(self):
        return print("Action : " + str(self.index) + " / "+ self.type + " / " + self.time + " / (" + str(self.position) + ") " + self.text)
