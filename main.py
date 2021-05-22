from core import my_gui, gui_action


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
