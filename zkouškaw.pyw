import tkinter

class MainWindow(tkinter.Frame):

	def __init__(self,parent):
		super().__init__(parent)
		self.parent = parent
		self.parent.title("První GUI aplikace")
		self.create_widgets()
		self.parent.minsize(500, 200) # minimální velisost
		self.parent.maxsize(1000, 600) # maximální velikost
		self.parent.resizable(True, True) # je okno měnitelné
		self.aa = 0


	def create_widgets(self):
		self.label = tkinter.Label(text="Hello světe")
		self.label.grid(row=0,column=0)
		self.button = tkinter.Button(text="Klikni hovado!",command=self.klikni)
		self.button.grid(row=0,column=1)
		self.button2 = tkinter.Button(text="Neuvěřitelné!",command=self.klikni2)
		self.button2.grid(row = 0,column = 2)
	def klikni(self):
		self.aa += 1
		if(self.button["foreground"]!="blue"):
			self.button["foreground"]="blue"
			self.button["text"]="To je ale švanda"
		else:
			self.button["foreground"]="green"
			self.button["text"]="To je ale švanda"
		self.label.config(text=self.button["foreground"]+str(self.aa)+"Příliš žluťoučký kůň ")
	def klikni2(self):
		self.label.config(text="Testovací hovadina")




root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()
