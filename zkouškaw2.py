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
		self.label = tkinter.Label(text="Hello world")
		self.label.grid(row=0,column=0)
		self.button = tkinter.Button(text="Klikni hovado!",command=self.klikni)
		self.button.grid(row=0,column=1)
	def klikni(self):
		self.aa += 1
		if(self.button["foreground"]!="blue"):
			self.button["foreground"]="blue"
		else:
			self.button["foreground"]="red"
		self.label.config(text=self.button["foreground"]+str(self.aa)+"Příliš žluťoučký kůň ")
		
		
		

root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()