from core import my_gui, my_parser
import threading
from time import sleep
from tkinter import filedialog

def start(app):
	actions_list = my_parser.parse(app.getFile().strip())

	reader = threading.Thread(target=lambda:readAction(app,actions_list,True),name="reader", daemon=True)
	reader.start()

def readAction(app, actions_list, run):
	print("thread")
	app.reset()
	start = app.getStart()
	for action in actions_list[:start]:
		if not run:
			break
		if action.type == "ins":
			app.insert(action.text, action.position)
		elif action.type == "back":
			app.delete(action.text, action.position)

	for action in actions_list[start:]:
		if not run:
			break
		if action.type == "ins":
			app.insert(action.text, action.position)
		elif action.type == "back":
			app.delete(action.text, action.position)
		sleep(0.1)

def openFile(app):
	app.fileInput = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("ses files","*.ses"),("all files","*.*")))
	app.displayFile()