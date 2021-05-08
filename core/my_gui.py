import tkinter as tk


class App(object):

    def __init__(self, gui_action):
        parent = tk.Tk()
        parent.geometry("300x400")
        self.root = parent
        self.root.title("Schnappi viewer")
        self.root.rowconfigure(4, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, minsize=300, weight=1)

        self.frame = tk.Frame(self.root, height=300, bg="white", pady=5, padx=5)
        self.frame.grid(row=2, column=0, sticky="nsew", columnspan=2)
        self.main_text = tk.Label(self.frame, justify="left", fg="black", bg="white", anchor="nw")
        self.file_label = tk.Label(self.root)
        self.file_label.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.choose_file = tk.Button(self.root, text="Open file", command=lambda: gui_action.open_file(self))
        self.choose_file.grid(row=0, column=0, columnspan=2)
        self.start = tk.Button(self.root, text="PLAY", state="disabled", command=lambda: gui_action.start(self), height=2, width=6)
        self.start.grid(row=3, column=0)
        self.slider = tk.Scale(self.root, from_=0, to=0, orient="horizontal", sliderrelief='flat', highlightthickness=0)
        self.slider.grid(row=3, column=1, sticky="nsew")

    def get_file(self):
        return self.file_input.strip()

    def insert(self, char, position):
        print("Ajout : " + char)
        char_list = list(self.main_text.cget("text"))
        if char == "&#xa;":
            char = "\n"

        if len(char_list) > int(position):
            char_list[int(position)] = char
            self.main_text.configure(text="".join(char_list))
        else:
            self.main_text.configure(text=self.main_text.cget("text") + char)

    def set_slider_max(self, value):
        self.slider.configure(to=value)

    def delete(self, char, position):
        print("Suppression : " + char)
        char_list = list(self.main_text.cget("text"))
        if char == "&#xa;":
            char = "\n"
        if len(char_list) > int(position) and char_list[int(position)] == char:
            char_list.pop(int(position))
            self.main_text.configure(text="".join(char_list))

    def reset(self):
        self.main_text.configure(text="")

    def display_file(self):
        name = self.file_input.split('/')
        self.choose_file.configure(text=name[-1])
        # self.file_label.configure(text=name[len(name)-1])

    def get_start(self):
        return self.slider.get()

    def update_start(self, value):
        self.slider.set(value)

    def init(self):
        print('test')
        self.main_text.pack(fill="both", expand=1)
    # self.chooseFile.pack()
    # self.fileLabel.pack()
    # self.frame.pack()
    # self.start.pack()
    # self.mainText.pack()
    # self.slider.pack()
