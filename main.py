from core import my_gui, my_parser
import tkinter as tk
from time import sleep


def main():
	fileName = 'schnappi.ses'

	root = tk.Tk()

	app = my_gui.App(root)
	file = app.getFile
	B = tk.Button(root, text ="Run", command = lambda: start(root, app, file))
	B.pack()
	app.init()
	root.mainloop()




def start(root, app, file):
	actions_list = my_parser.parse(file().strip())
	app.reset()
	for action in actions_list:
		if action.type == "ins":
			app.insert(action.text, action.position)
		elif action.type == "back":
			app.delete(action.text, action.position)


if __name__ == "__main__":
	main()
