import tkinter as tk


class App(object):

    def __init__(self, parent):
        parent.geometry("400x600")
        self.root = parent
        self.root.title("Schnappi viewer")
        self.frame = tk.Frame(parent)
        self.label = tk.Label()
        self.frame.pack()
        self.label.pack()

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
            self.label.configure(text="".join(char_list))
