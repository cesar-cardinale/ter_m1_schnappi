from core import my_gui, my_parser
import tkinter as tk


def main():
    file = 'schnappi.ses'

    actions_list = my_parser.parse(file)

    root = tk.Tk()
    app = my_gui.App(root)
    for action in actions_list:
        if action.type == "ins":
            app.insert(action.text, action.position)
        elif action.type == "back":
            app.delete(action.text, action.position)
    root.mainloop()


if __name__ == "__main__":
    main()
