from core import my_gui, my_parser
import threading
from time import sleep
from tkinter import filedialog


def start(app_gui):
    run = threading.Event()
    reader = threading.Thread(target=read_action, args=(app_gui, app_gui.actions_list, run), name="reader", daemon=True)
    reader.start()
    app_gui.start.configure(text='PAUSE', command=lambda: pause(app_gui, run))


def pause(app_gui, run):
    run.set()
    change_button(app_gui)


def change_button(app_gui):
    app_gui.start.configure(text='PLAY', command=lambda: start(app_gui))


def read_action(app_gui, actions_list, run):
    print("thread")
    app_gui.reset()
    gui_start = app_gui.get_start()
    for action in actions_list[:gui_start]:
        if action.type == "ins":
            app_gui.insert(action.text, action.position)
        elif action.type == "back":
            app_gui.delete(action.text, action.position)

    for action in actions_list[gui_start:]:
        update_slider(app_gui, actions_list.index(action))
        if run.is_set():
            update_slider(app_gui, actions_list.index(action))
            return
        if action.type == "ins":
            app_gui.insert(action.text, action.position)
        elif action.type == "back":
            app_gui.delete(action.text, action.position)
        sleep(0.1)
    update_slider(app_gui, len(actions_list))
    change_button(app_gui)


def update_slider(app_gui, value):
    app_gui.update_start(value)


def open_file(app_gui):
    app_gui.reset()
    update_slider(app_gui, 0)
    app_gui.file_input = filedialog.askopenfilename(initialdir="./", title="Select file",
                                                    filetypes=(("ses files", "*.ses"), ("all files", "*.*")))
    if app_gui.file_input:
        app_gui.display_file()
        app_gui.start.configure(state="normal")
        app_gui.actions_list = my_parser.parse(app_gui.get_file().strip())
        app_gui.set_slider_max(len(app_gui.actions_list))
