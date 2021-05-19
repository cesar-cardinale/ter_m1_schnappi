import tkinter

from core import my_parser, my_gui
import threading
from time import sleep
from tkinter import filedialog

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


def slider_callback(_):
    if run.is_set():
        jump()


def jump():
    app_gui.reset()
    gui_start = app_gui.get_start()
    for action in app_gui.actions_list[:gui_start]:
        if action.type == "ins":
            app_gui.insert(action.text, action.position)
        elif action.type == "back":
            app_gui.delete(action.text, action.position)


def read_action():
    gui_start = app_gui.get_start()
    for action in app_gui.actions_list[gui_start:]:
        update_slider(app_gui.actions_list.index(action))
        if run.is_set():
            update_slider(app_gui.actions_list.index(action))
            return
        if action.type == "ins":
            app_gui.insert(action.text, action.position)
        elif action.type == "back":
            app_gui.delete(action.text, action.position)
        sleep(app_gui.speed.get())
    update_slider(len(app_gui.actions_list))
    run.set()
    change_button()


def update_slider(value):
    app_gui.update_start(value)


def open_file(gui):
    global app_gui
    app_gui = gui
    app_gui.reset()
    update_slider(0)
    app_gui.file_input = filedialog.askopenfilename(initialdir="./", title="Select file",
                                                    filetypes=(("ses files", "*.ses"), ("all files", "*.*")))
    if app_gui.file_input:
        app_gui.display_file()
        app_gui.start.configure(state="normal")
        app_gui.actions_list = my_parser.parse(app_gui.get_file().strip())
        app_gui.set_slider_max(len(app_gui.actions_list))
        app_gui.set_slider_callback(slider_callback)
