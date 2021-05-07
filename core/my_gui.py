import tkinter as tk



class App(object):

    def __init__(self,gui_action):
        parent = tk.Tk()
        parent.geometry("400x300")
        self.root = parent
        self.root.title("Schnappi viewer")
        self.frame = tk.Frame(self.root)
        self.mainText = tk.Label(self.root,bg = "white", justify="left")
        self.fileLabel = tk.Label(self.root)
        self.chooseFile = tk.Button(self.root, text ="Open file", command = lambda: gui_action.openFile(self))
        self.start = tk.Button(self.root, text ="Run", command = lambda: gui_action.start(self))
        self.slider = tk.Scale(self.root, from_=0, to=200,orient="horizontal")
        
        
    def getFile(self):
        return self.fileInput.strip()

    def insert(self, char, position):
        print("Ajout : "+char)
        char_list = list(self.mainText.cget("text"))
        if char == "&#xa;":
            char = "\n"

        if len(char_list) > int(position):
            char_list[int(position)] = char
            self.mainText.configure(text="".join(char_list))
        else:
            self.mainText.configure(text=self.mainText.cget("text") + char)


    def setSliderMax(self, value):
        self.slider.configure(to = value)

    def delete(self, char, position):
        print("Suppression : "+char)
        char_list = list(self.mainText.cget("text"))
        if char == "&#xa;":
            char = "\n"
        if len(char_list) > int(position) and char_list[int(position)] == char:
            char_list.pop(int(position))
            self.mainText.configure(text = "".join(char_list))
    
    def reset(self):
        self.mainText.configure(text = "")

    def displayFile(self):
        self.fileLabel.configure(text = self.fileInput)

    def getStart(self):
        return self.slider.get()

    def updateStart(self, value):
        self.slider.set(value)


    def init(self):
        self.chooseFile.pack()
        self.fileLabel.pack()
        self.frame.pack()
        self.start.pack()
        self.mainText.pack()
        self.slider.pack()