import tkinter as tk



class App(object):

    def __init__(self,gui_action):
        parent = tk.Tk()
        parent.geometry("400x300")
        self.root = parent
        self.startingpoint = tk.Text(self.root, height = 1,width = 20,bg = "light yellow")
        self.root.title("Schnappi viewer")
        self.frame = tk.Frame(self.root)
        self.label = tk.Label(self.root)
        self.fileLabel = tk.Label(self.root)
        self.chooseFile = tk.Button(self.root, text ="Open file", command = lambda: gui_action.openFile(self))
        self.start = tk.Button(self.root, text ="Run", command = lambda: gui_action.start(self))
        
        
    def getFile(self):
        return self.fileInput.strip()

    def insert(self, char, position):
        print("Ajout : "+char)
        char_list = list(self.label.cget("text"))
        if char == "&#xa;":
            char = "\n"

        if len(char_list) > int(position):
            char_list[int(position)] = char
            self.label.configure(text="".join(char_list))
        else:
            self.label.configure(text=self.label.cget("text") + char)

    def delete(self, char, position):
        print("Suppression : "+char)
        char_list = list(self.label.cget("text"))
        if char == "&#xa;":
            char = "\n"
        if len(char_list) > int(position) and char_list[int(position)] == char:
            char_list.pop(int(position))
            self.label.configure(text = "".join(char_list))
    
    def reset(self):
        self.label.configure(text = "")

    def displayFile(self):
        self.fileLabel.configure(text = self.fileInput)

    def getStart(self):
        return int(self.startingpoint.get("1.0" ,"end").strip())


    def init(self):
        self.chooseFile.pack()
        self.fileLabel.pack()
        self.frame.pack()
        self.startingpoint.pack()
        self.start.pack()
        self.label.pack()