class Action:
    def __init__(self, type, time, text, position):
        self.type = type
        self.time = time
        self.text = text
        self.position = position

    def to_cli(self):
        return print("Action : " + self.type + " / " + self.time + " / (" + str(self.position) + ") " + self.text)
