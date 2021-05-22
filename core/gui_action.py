import tkinter as tk

from core import my_parser
import threading
from time import sleep
from tkinter import filedialog

global previous
previous = 0
global app_gui
global run
run = threading.Event()
run.set()


def start():
    global run
    run = threading.Event()
    reader = threading.Thread(target=thread_read, name="reader", daemon=True)
    reader.start()
    app_gui.start.configure(text='PAUSE', command=pause)


def pause():
    run.set()
    change_button()


def change_button():
    app_gui.set_slider_callback(slider_callback)
    app_gui.start.configure(text='PLAY', command=lambda: start())


def thread_read():
    read_action()


def slider_callback(target):
    if run.is_set():
        jump(target)


def jump(target):
    target = int(target)
    if target > previous:
        read_forward(target)
    elif target < previous:
        read_backward(target)
    app_gui.main_text.yview(tk.END)
    update_slider(target)


def read_forward(target):
    for action in app_gui.actions_list[previous:target]:
        if action.type == "ins":
            app_gui.insert(action.text, action.position, 'forward')
        elif action.type == "back":
            app_gui.delete(action.text, action.position, 'forward')
        elif action.type == "del":
            for c in action.text:
                app_gui.delete(c, action.position, 'forward')


def read_backward(target):
    sub_action = app_gui.actions_list[target:previous]
    for action in sub_action[::-1]:
        if action.type == "ins":
            app_gui.delete(action.text, action.position, 'backward')
        elif action.type == "back":
            app_gui.insert(action.text, action.position, 'backward')
        elif action.type == "del":
            for c in action.text:
                app_gui.insert(c, action.position, 'backward')


def read_action():
    gui_start = app_gui.get_slider_position()
    for action in app_gui.actions_list[gui_start:]:
        jump(action.index + 1)
        update_slider(action.index + 1)
        sleep(app_gui.speed.get())
        if run.is_set():
            return

    run.set()
    change_button()


def update_slider(value):
    app_gui.update_slider(value)
    global previous
    previous = value


def open_file(gui):
    global app_gui
    app_gui = gui
    update_slider(0)
    app_gui.file_input = filedialog.askopenfilename(initialdir="./", title="Select file",
                                                    filetypes=(("ses files", "*.ses"), ("all files", "*.*")))
    if app_gui.file_input:
        app_gui.reset()
        app_gui.display_file()
        app_gui.start.configure(state="normal")
        app_gui.actions_list = my_parser.parse(app_gui.get_file().strip())
        app_gui.set_slider_max(len(app_gui.actions_list))
        app_gui.set_slider_callback(slider_callback)
