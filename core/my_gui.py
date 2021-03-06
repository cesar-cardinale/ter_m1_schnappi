import tkinter as tk
from tkinter.scrolledtext import *
from model.schnappi_string_element import Schnappi_string_element as text_element


class App(object):

    def __init__(self, gui_action):
        self.text = []

        self.file_input = None
        parent = tk.Tk()
        parent.geometry("500x700")
        parent.minsize("500", "700")
        self.root = parent
        self.root.title("Schnappi viewer")

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.frame = tk.Frame(self.root, height=800, width=500, bg="#DED6C9", pady=5, padx=5)
        self.frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.frame.grid(row=2, column=0, sticky="nsew", columnspan=4)
        self.main_text = ScrolledText(self.frame, fg="black", bg="#DED6C9", wrap=tk.WORD)
        self.text_tags_init()

        self.file_label = tk.Label(self.root)
        self.file_label.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.choose_file = tk.Button(self.root, text="Open file", command=lambda: gui_action.open_file(self))
        self.choose_file.grid(row=0, column=0, columnspan=2)

        self.start = tk.Button(self.root, text="PLAY", state="disabled", command=lambda: gui_action.start(), height=2,
                               width=5)
        self.start.grid(row=3, column=0, sticky="nsew")

        self.slider = tk.Scale(self.root, from_=0, to=0, orient="horizontal", sliderrelief='flat', highlightthickness=0)
        self.slider.grid(row=3, column=1, sticky="nsew")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open file ...", command=lambda: gui_action.open_file(self))
        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.speed = tk.DoubleVar()
        self.speed.set(.05)
        submenu = tk.Menu(menubar, tearoff=0)
        submenu.add_radiobutton(label="25ms", value=.025, variable=self.speed)
        submenu.add_radiobutton(label="50ms", value=.05, variable=self.speed)
        submenu.add_radiobutton(label="100ms", value=.1, variable=self.speed)
        submenu.add_radiobutton(label="500ms", value=.5, variable=self.speed)
        menubar.add_cascade(label="Speed", menu=submenu, underline=0)

    def get_file(self):
        return self.file_input.strip()

    def set_slider_max(self, value):
        self.slider.configure(to=value)

    def set_slider_callback(self, function):
        self.slider.configure(command=function)

    # insert in the text widget and self.text
    def insert(self, char, position, direction):
        print("Ajout : " + char + " position : " + str(position))
        char_list = self.text.copy()

        if direction == 'forward':
            main_text_pos = self.get_position_text(position, False)
            element = text_element(char, [])
            if len(char_list) > position:
                char_list.insert(position, element)
                self.main_text.insert(main_text_pos, element.char, 'normal')
            else:
                char_list.append(element)
                self.main_text.insert(main_text_pos, char, 'normal')

        elif direction == 'backward':
            main_text_pos = self.get_position_text(position, True)
            if char_list[position - 1].del_after:
                element = char_list[position - 1].del_after[-1]
                char_list[position - 1].del_after.pop(-1)
            else:
                element = text_element(char, ())

            if element.char == '\n':
                self.main_text.delete(main_text_pos)
            self.main_text.delete(main_text_pos)
            self.main_text.insert(main_text_pos, element.char, 'normal')
            if len(char_list) > position:
                char_list.insert(position, element)
            else:
                char_list.append(element)
        self.text = char_list
        self.main_text.yview(tk.END)

    # delete in the text widget and self.text
    def delete(self, char, position, direction):
        print("Suppression : " + char + " position : " + str(position))
        char_list = self.text.copy()
        #print(len(char_list))
        if len(char_list) > position:
            if direction == 'forward':
                main_text_pos = self.get_position_text(position, False)
                if char_list[position].char == '\n':
                    self.main_text.delete(main_text_pos)
                    self.main_text.insert(main_text_pos, '\\n', 'deleted')
                else:
                    self.main_text.tag_add('deleted', main_text_pos)
                char_list[position - 1].append_all_after(char_list[position])
            elif direction == 'backward':
                main_text_pos = self.get_position_text(position, False)
                self.main_text.delete(main_text_pos)

            char_list.pop(position)
            self.text = char_list.copy()
            self.main_text.yview(tk.END)


    # give the position in the text widget
    def get_position_text(self, pos, sup):
        line = 1
        pos_last_new_line = 0
        index = 0

        for i, c in enumerate(self.text[:pos]):
            if c.char == '\n':
                line += 1
                pos_last_new_line = i+1

        for i, c in enumerate(self.text[pos_last_new_line:pos]):
            index += len(c.get_string())

        if sup and self.text[pos - 1].del_after :
            index -= len(self.text[pos - 1].del_after[-1].get_string())

        print(line, index)
        return str(line) + '.' + str(index)

    def reset(self):
        self.text = []
        self.main_text.delete(1.0, tk.END)

    def display_file(self):
        name = self.file_input.split('/')
        self.choose_file.configure(text=name[-1])
        self.file_label.configure(text=name[-1])

    def get_slider_position(self):
        return self.slider.get()

    def update_slider(self, value):
        self.slider.set(value)

    def init(self):
        self.main_text.pack(fill="both", expand=1)

    def text_tags_init(self):
        self.main_text.tag_configure('normal', overstrike=0, foreground="#000000")
        self.main_text.tag_configure('deleted', overstrike=1, foreground="#CD5C5C")

    def print_text(self):
        for c in self.text:
            print(c.char, end=' : ')
            for d in c.del_after:
                print(d.get_string())
            print('')

    def on_exit(self):
        self.root.quit()
