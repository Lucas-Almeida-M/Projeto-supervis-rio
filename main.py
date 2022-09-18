from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from turb import Turbina
from paginc import PageOne
from hel import Helice
from conv import Conversores
from bat import Bateria
import json


class App ( Tk ):


	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		container = Frame(self)
		container.grid(row=0,column=0)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)


		f = open('config.json','r')
		configs = json.load(f)
		f.close()


		self.modbus_addrs = {
			'FT_001':[1000,1],
			'FT_002':[1001,1],
			'PT_001':[1002,100],
			'PT_002':[1003,100],
			'PT_003':[1004,100],
			'PT_004':[1005,100],
			'TE_001':[1006,10],
			'TE_002':[1007,10],
			'TE_003':[1008,10],
			'TT_001':[1009,10],
			'TT_002':[1010,10],
			'TT_003':[1011,10],
			'FZ_003':[1012,1],
			'FZ_001':[1013,1],
			'FZ_002':[1014,1],
			'SV_001':[1015,1],
			'SV_002':[1016,1],
			'SV_003':[1017,1],
			'SV_004':[1018,1],
			'SV_005':[1019,1],
			'SV_006':[1020,1],
			'SV_007':[1021,1],
			'SV_008':[1022,1],
			'LSH_001':[1023,1],
			'LSL_001':[1024,1],
			'LSL_002':[1025,1],
			'BY_001':[1026,1],
			'FY_001':[1027,1],
			'FY_002':[1028,1],
			'FY_003':[1029,1],
			'EE_101':[2000,1],
			'EE_102':[2001,1],
			'EE_103':[2002,1],
			'IE_101':[2003,1],
			'IE_102':[2004,1],
			'IE_103':[2005,1],
			'TE_101':[2006,1],
			'SE_101':[2007,1],
			'EE_201':[2008,1],
			'EE_202':[2009,1],
			'IE_201':[2010,1],
			'TE_201':[2011,1],
			'TE_202':[2012,1],
			'EE_301':[2013,1],
			'EE_302':[2014,1],
			'EE_303':[2015,1],
			'IE_301':[2016,1],
			'IE_302':[2017,1],
			'IE_303':[2018,1],
			'TE_301':[2019,1],
			'ST_301':[2020,1],
			'WT_401':[3000,1],
			'TE_401':[3001,1],
			'WT_402':[3002,1],
			'TE_402':[3003,1],
			'LG_DES':[4000,1],
			'CLP':[4001,1],
		}

		self.frames = {}
		for F in (PageOne, Turbina, Helice, Conversores, Bateria):
			page_name = F.__name__
			frame = F(configs,self.modbus_addrs ,parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("PageOne")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()
		


if __name__ == '__main__':
	def SetSize():
		width, height, X_POS, Y_POS = a.winfo_width(), a.winfo_height(), a.winfo_x(), 0
		a.state('normal')
		a.resizable(0,0)
		a.geometry("%dx%d+%d+%d" % (width, height, X_POS, Y_POS))
	a = App()
	a.call("source", "sun-valley.tcl")
	a.call("set_theme", "light")
	a.iconbitmap("./img/icone.ico")
	a.title('Supervisório LAPHE - v1.0')
	a.state('zoomed')
	SetSize()
	a.mainloop()



	