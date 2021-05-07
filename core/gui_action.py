from core import my_gui, my_parser
import threading
from time import sleep
from tkinter import filedialog

def start(appGui):
	run = threading.Event()
	reader = threading.Thread(target=readAction,args=(appGui,appGui.actions_list,run),name="reader", daemon=True)
	reader.start()
	appGui.start.configure(text = 'Stop', command = lambda : pause(appGui,run))


def pause(appGui, run):
	run.set()
	changeButton(appGui)

def changeButton(appGui):
	appGui.start.configure(text = 'Run', command = lambda : start(appGui))

def readAction(appGui, actions_list, run):
	print("thread")
	appGui.reset()
	start = appGui.getStart()
	for action in actions_list[:start]:
		if action.type == "ins":
			appGui.insert(action.text, action.position)
		elif action.type == "back":
			appGui.delete(action.text, action.position)

	for action in actions_list[start:]:
		if run.is_set():
			updateSlider(appGui, actions_list.index(action))
			return
		if action.type == "ins":
			appGui.insert(action.text, action.position)
		elif action.type == "back":
			appGui.delete(action.text, action.position)
		sleep(0.1)
	updateSlider(appGui, len(actions_list))
	changeButton(appGui)

def updateSlider(appGui, value):
	appGui.updateStart(value)


def openFile(appGui):
	appGui.reset()
	updateSlider(appGui, 0)
	appGui.fileInput = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("ses files","*.ses"),("all files","*.*")))
	appGui.displayFile()
	appGui.actions_list = my_parser.parse(appGui.getFile().strip())
	appGui.setSliderMax(len(appGui.actions_list))