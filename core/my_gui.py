import tkinter as tk


class App(object):

    def __init__(self, gui_action):
        self.text = ""
        self.text_deleted = []

        self.file_input = None
        parent = tk.Tk()
        parent.geometry("500x700")
        parent.minsize("500", "700")
        self.root = parent
        self.root.title("Schnappi viewer")

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.frame = tk.Frame(self.root, height=800, width=500, bg="#b3a38e", pady=5, padx=5)
        self.frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.main_text = tk.Text(self.frame, fg="black", bg="#b3a38e")
        self.frame.grid(row=2, column=0, sticky="nsew", columnspan=4)
        scrollbar = tk.Scrollbar(self.frame)
        self.main_text = tk.Text(self.frame, fg="black", bg="#b3a38e", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.main_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_label = tk.Label(self.root)
        self.file_label.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.choose_file = tk.Button(self.root, text="Open file", command=lambda: gui_action.open_file(self))
        self.choose_file.grid(row=0, column=0, columnspan=2)

        self.start = tk.Button(self.root, text="PLAY", state="disabled", command=lambda: gui_action.start(), height=2, width=5)
        self.start.grid(row=3, column=0,sticky="nsew")

        self.slider = tk.Scale(self.root, from_=0, to=0, orient="horizontal", sliderrelief='flat', highlightthickness=0)
        self.slider.grid(row=3, column=1, sticky="nsew")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar,tearoff=0)
        file_menu.add_command(label="Open file ...", command=lambda: gui_action.open_file(self))
        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.speed = tk.DoubleVar()
        self.speed.set(.05)
        submenu = tk.Menu(menubar,tearoff=0)
        submenu.add_radiobutton(label="25ms", value=.025, variable=self.speed)
        submenu.add_radiobutton(label="50ms", value=.05, variable=self.speed)
        submenu.add_radiobutton(label="100ms", value=.1, variable=self.speed)
        submenu.add_radiobutton(label="500ms", value=.5, variable=self.speed)
        menubar.add_cascade(label="Speed", menu=submenu, underline=0)

    def get_file(self):
        self.reset()
        return self.file_input.strip()

    def insert(self, char, position):
        print("Ajout : " + char)
        char_list = self.text
        if len(char_list) > position:
            char_list = self.text[:int(position)]+char+self.text[int(position):]
            #char_list[int(position)] = char
            self.text = "".join(char_list)
            for item in self.text_deleted:
                if item[0] > position:
                    item[0] += 1
            self.display_text()
            # char_list[position] = char
            # self.reset()
            # self.main_text.insert(1.0, "".join(char_list))
        else:
            self.text += char
            self.main_text.insert(tk.END, char)

    def set_slider_max(self, value):
        self.slider.configure(to=value)

    def set_slider_callback(self, function):
        self.slider.configure(command=function)

    def delete(self, char, position):
        print("Suppression : " + char)
        char_list = list(self.text)
        if len(char_list) > position and char_list[position] == char:
            new_position = position
            for item in self.text_deleted:
                if item[0] == new_position:
                    new_position += 1
            self.text_deleted.append([new_position, char])
            char_list.pop(position)
            self.text = "".join(char_list)
            self.display_text()
        if len(char_list) > position:
            for item in self.text_deleted:
                if item[0] > position:
                    item[0] -= 1

    def reset(self):
        self.text = ""
        self.main_text.delete(1.0, tk.END)
        self.text_deleted = []

    def display_file(self):
        name = self.file_input.split('/')
        self.choose_file.configure(text=name[-1])
        self.file_label.configure(text=name[-1])

    def get_start(self):
        return self.slider.get()

    def update_start(self, value):
        self.slider.set(value)

    def init(self):
        self.main_text.pack(fill="both", expand=1)

    def on_exit(self):
        self.root.quit()

    def display_text(self):
        words = []
        self.text_deleted.reverse()
        first_deleted = 0
        last_deleted = 0
        last_word = ""
        for i, char in enumerate(self.text_deleted):
            if i == len(self.text_deleted) - 1:
                last_word += char[1]
                words.append([first_deleted, last_word])
            elif char[0] == last_deleted + 1:
                last_deleted = char[0]
                last_word += char[1]
            else:
                words.append([first_deleted, last_word])
                first_deleted = char[0]
                last_word = char[1]
                last_deleted = char[0]

        # print(JSONEncoder.encode(JSONEncoder(), self.text_deleted))
        final_text = []
        last_deleted = 0
        for i, char in enumerate(self.text):
            for word in words:
                if i == word[0] - 1:
                    final_text.append("[" + word[1] + "]")
            # for char2 in self.text_deleted:
            #     # print(i, last_deleted)
            #     if i == char2[0]-1 or last_deleted+1 == char2[0]:
            #         final_text.append('|'+char2[1]+'|')
            #         last_deleted = char2[0]
            final_text.append(char)
        self.text_deleted.reverse()
        self.main_text.delete(1.0, tk.END)
        self.main_text.insert(1.0, "".join(final_text))

    # self.chooseFile.pack()
    # self.fileLabel.pack()
    # self.frame.pack()
    # self.start.pack()
    # self.mainText.pack()
    # self.slider.pack()
