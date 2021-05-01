from core import my_gui, my_parser, gui_action
import tkinter as tk
from time import sleep
import threading

def main():

	app = my_gui.App(gui_action)
	
	app.init()
	app.root.mainloop()






# def getReaderThread():
# 	for t in threading.enumerate():
# 		if t.name == "reader":
# 			return t




if __name__ == "__main__":
	main()
