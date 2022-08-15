import gi 

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk , Gdk

class Main(Gtk.Window):
	"""docstring for Main"""
	def __init__(self):
		self.num = None
		self.var = None
		size=300
		super().__init__(title="Calculator")
		
		self.set_default_size(size,size)
		
		
		self.label  = Gtk.Label()
		self.label.set_text("")
		self.label.get_style_context().add_class("lbl")
		self.label.set_xalign(1)
		self.label.set_size_request(size//4, size//4)

		self.smlabel  = Gtk.Label()
		self.smlabel.set_text("")
		self.smlabel.get_style_context().add_class("smlbl")
		self.smlabel.set_xalign(1)
		self.smlabel.set_size_request(size//5, size//5)

		box = Gtk.Box()
		box.set_orientation(Gtk.Orientation.VERTICAL)
		box.add(self.smlabel)
		box.add(self.label)


		backbtn = Gtk.Button(label="CE")

		button0 = Gtk.Button(label="0")
		button1 = Gtk.Button(label="1")
		button2 = Gtk.Button(label="2")
		button3 = Gtk.Button(label="3")
		button4 = Gtk.Button(label="4")
		button5 = Gtk.Button(label="5")
		button6 = Gtk.Button(label="6")
		button7 = Gtk.Button(label="7")
		button8 = Gtk.Button(label="8")
		button9 = Gtk.Button(label="9")
		buttonadd = Gtk.Button(label="+")
		buttondiv = Gtk.Button(label="/")
		buttonmul = Gtk.Button(label="*")
		buttonsub = Gtk.Button(label="-")
		enterbtn = Gtk.Button(label="=")
		backbtn.get_style_context().add_class("backbtn")
		enterbtn.get_style_context().add_class("enterbtn")
		btns = [enterbtn,backbtn,button0,button1,button2,button3,button4,button5,button6,button7,button8,button9,buttonadd,buttonsub,buttonmul,buttondiv]	
		for i in btns:
			i.set_size_request(size//3, size//3)
			i.connect("clicked",self.OnClick)
		
		grid = Gtk.Grid()
		grid.set_column_spacing(3)

		
		grid.add(button0)
		grid.attach_next_to(box,button0,Gtk.PositionType.TOP,4,1)
		grid.attach(backbtn,1,0,1,1)
		grid.attach(enterbtn,2,0,1,1)
		grid.attach(buttonadd,3,0,1,1)

		grid.attach(button1,0,1,1,1)
		grid.attach(button2,1,1,1,1)
		grid.attach(button3,2,1,1,1)
		grid.attach(buttonsub,3,1,1,1)

		grid.attach(button4,0,2,1,1)
		grid.attach(button5,1,2,1,1)
		grid.attach(button6,2,2,1,1)
		grid.attach(buttonmul,3,2,1,1)

		grid.attach(button7,0,3,1,1)
		grid.attach(button8,1,3,1,1)
		grid.attach(button9,2,3,1,1)
		grid.attach(buttondiv,3,3,1,1)

		
		self.add(grid)


	def OnClick(self,btn):
		cur = btn.get_label()
		if(cur =="CE"):
			self.var=None
			self.num=None
			self.label.set_text("")
			self.smlabel.set_text("")
			
		elif(cur=="=" and self.num != None and self.var != None):
			self.label.set_text(str(eval(self.num+self.var+self.label.get_text())))
			self.var=None
			self.num=None
			self.smlabel.set_text("")
		elif(cur in ["+","-","/","*"]):
			if(self.var != None):
				self.var=cur
				print(self.num)
				self.num =self.num[:len(self.num)-1]+self.var
				self.smlabel.set_text(self.num)
			else:
				self.num=self.label.get_text()
				self.var=cur
				self.smlabel.set_text(self.num+self.var)
				self.label.set_text("")
		elif(cur in [str(i) for i in range(0,10)]):
			self.label.set_text(self.label.get_text() + cur)



css = b'''* { font-size: 2rem; }
	.lbl {font-weight : bold }
	.smlbl {color : grey}
	.backbtn {background-color: #11dbed ; color:black }
	.enterbtn {background-color: #57ed11; color : black}
'''
css_provider = Gtk.CssProvider()
css_provider.load_from_data(css)
context = Gtk.StyleContext()
screen = Gdk.Screen.get_default()
context.add_provider_for_screen(screen, css_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)



win = Main()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()