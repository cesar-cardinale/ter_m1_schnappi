import multiprocessing
class ReaderThread:
	def __init__(self, funtion):
		self.thread = threading.Thread(target= funtion, name="reader", daemon= True)

	def start():
		self.thread.start()