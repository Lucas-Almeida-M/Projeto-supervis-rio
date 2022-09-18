from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import Button as SButton
from tkinter import Label as SLabel
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
from PIL import ImageTk, Image
style.use("dark_background")


class Bateria( Frame ):



	def __init__(self,configs,modbus_addrs,parent, controller):
		Frame.__init__(self, parent)

		#self.grid(padx=5,pady=5)
		self.controller = controller
		#self.title = title
		#self.icon = icon
		#self.root.title(title)
		#self.root.iconbitmap(icon)
		# self.option_add('*tearOff', FALSE)

		# menubar = Menu(self)
		# filemenu = Menu(menubar)
		# filemenu.add_command(label="Open")
		# filemenu.add_command(label="Save")
		# filemenu.add_command(label="Exit")
		# menubar.add_cascade(label="File", menu=filemenu)
		# self.config(menu=menubar)

		self.xList = []
		self.yList = []
		self.ybList = []
		self.ycList = []
	

		
		self.status = LabelFrame(self,text='STATUS',border=40,padding=10)
		self.status.grid(row=0,column=0,columnspan=2,rowspan=4,padx=10,pady=5,sticky="nw")



		lturb = Label(self.status,text='Baterias:',font=("Arial", 14),padding=(0,0,0,25))
		lturb.grid(row=0,column=0,padx=35)
		self.turb = SLabel(self.status,text='Descarregadas',font=("Arial", 14),fg='#f00')
		self.turb.grid(row=1,column=0)
		s1 = Separator(self.status, orient=HORIZONTAL)
		s1.grid(row=2,column=0, sticky="ew",pady=30)
		lfalha = Label(self.status,text='Falhas:',font=("Arial", 14),padding=(0,0,0,10))
		lfalha.grid(row=3,column=0)
		self.falha = SLabel(self.status,text='---------',font=("Arial", 14),fg='#0f0')
		self.falha.grid(row=4,column=0)


		lbat = Canvas(self, width=600, height=388)
		lbat.grid(row=0,column=2,columnspan=4,rowspan=4,padx=10,pady=45)
		batimg = (Image.open("img/pagbat.png"))
		resized_image= batimg.resize((600,388), Image.ANTIALIAS)
		new_image= ImageTk.PhotoImage(resized_image)
		self.new_image = new_image
		lbat.create_image(600, 388, image=new_image,anchor='se')



		bhome = Button(self, text="HOME", command=lambda: controller.show_frame("PageOne"))
		bhome.grid(row=2,column=0,sticky='we',padx=10,pady=50)

		bconfig = Button(self, text="Configurações", command=self.controller.frames['PageOne'].configuracoes)
		bconfig.grid(row=3,column=0,sticky='nwe',padx=10)

		bexpdados = Button(self, text="Exportar Dados", command=self.controller.frames['PageOne'].exportar)
		bexpdados.grid(row=3,column=1,sticky='nwe',padx=10)

		bhistdados = Button(self, text="Histórico de Dados", command=self.controller.frames['PageOne'].historico)
		bhistdados.grid(row=2,column=1,sticky='we',padx=10)





		self.temp = Label(self,text='   ----',font=("Arial", 14))
		self.temp.place(x=400,y=95)
		self.corr = Label(self,text='   ----',font=("Arial", 14))
		self.corr.place(x=580,y=95)
		self.ten = Label(self,text='   -----',font=("Arial", 14))
		self.ten.place(x=760,y=95)

		ltemp = Label(self,text='°C',font=("Arial", 14))
		ltemp.place(x=440,y=95)
		lcorr = Label(self,text='A',font=("Arial", 14))
		lcorr.place(x=620,y=95)
		lten = Label(self,text='V',font=("Arial", 14))
		lten.place(x=810,y=95)




		self.fcorr = Figure(figsize=(4.7, 2.3))
		self.acorr = self.fcorr.add_subplot(111)
		self.acorr.set_xlim(0,configs['bxlim'])
		self.acorr.set_ylim(0,configs['bcylim'])
		self.acorr.set_ylabel("Corrente [A]")
		self.line1 = self.acorr.plot([],[],color="blue")[0]
		# self.atorque.legend(handles=[self.line1],loc='upper right')

		self.canvascorr = FigureCanvasTkAgg(self.fcorr,master=self)
		self.canvascorr.get_tk_widget().grid(row=0,column=8)
		self.canvascorr.draw()



		self.ft = Figure(figsize=(4.7, 2.3))
		self.at = self.ft.add_subplot(111)
		self.at.set_xlim(0,configs['bxlim'])
		self.at.set_ylim(0,configs['btylim'])
		self.at.set_ylabel("Tensão [V]")
		self.line2 = self.at.plot([],[],color="blue")[0]
		# self.aemp.legend(handles=[self.line2],loc='upper right')

		self.canvastensao = FigureCanvasTkAgg(self.ft,master=self)
		self.canvastensao.get_tk_widget().grid(row=1,column=8,rowspan=2)
		self.canvastensao.draw()



		self.ftemperatura = Figure(figsize=(4.7, 2.4))
		self.atemperatura = self.ftemperatura.add_subplot(111)
		self.atemperatura.set_xlim(0,configs['bxlim'])
		self.atemperatura.set_ylim(0,configs['btemplim'])
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line3 = self.atemperatura.plot([],[],color="blue")[0]

		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=3,column=8)
		self.canvastemperatura.draw()



	
	  

	def set_b(self,limcy,limty,limtempy,limx):

		self.acorr.clear()
		self.acorr.set_ylim(0,limcy)
		self.acorr.set_xlim(0,limx)
		
		self.acorr.set_ylabel("Corrente [A]")
		self.line1 = self.acorr.plot([],[],color="blue")[0]
		# self.atorque.legend(handles=[self.line1],loc='upper right')

		self.canvascorr.get_tk_widget().delete()
		self.canvascorr = FigureCanvasTkAgg(self.fcorr,master=self)
		self.canvascorr.get_tk_widget().grid(row=0,column=8)
		self.canvascorr.draw()



		self.at.clear()
		self.at.set_xlim(0,limx)
		self.at.set_ylim(0,limty)
		self.at.set_ylabel("Tensão [V]")
		self.line2 = self.at.plot([],[],color="blue")[0]
		# self.aemp.legend(handles=[self.line2],loc='upper right')

		self.canvastensao.get_tk_widget().delete()
		self.canvastensao = FigureCanvasTkAgg(self.ft,master=self)
		self.canvastensao.get_tk_widget().grid(row=1,column=8,rowspan=2)
		self.canvastensao.draw()



		self.atemperatura.clear()
		self.atemperatura.set_xlim(0,limx)
		self.atemperatura.set_ylim(0,limtempy)
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line3 = self.atemperatura.plot([],[],color="blue")[0]
		self.canvastemperatura.get_tk_widget().delete()
		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=3,column=8)
		self.canvastemperatura.draw()





	def animate(self, dados):
		try:
			y = dados['values']['IE_201']
			yb = dados['values']['EE_202']
			yc = dados['values']['TE_202']
			

		except:
			y = 0
			yb = 0
			yc = 0


		if(len(self.yList)<int(self.acorr.get_xlim()[1])):
			self.yList.append(y)
			self.ybList.append(yb)
			self.ycList.append(yc)


		elif(len(self.yList)>=int(self.acorr.get_xlim()[1])):
			self.yList[0:int(self.acorr.get_xlim()[1])-1] = self.yList[1:int(self.acorr.get_xlim()[1])]
			self.yList[int(self.acorr.get_xlim()[1])-1] = int(y)
			self.ybList[0:int(self.acorr.get_xlim()[1])-1] = self.ybList[1:int(self.acorr.get_xlim()[1])]
			self.ybList[int(self.acorr.get_xlim()[1])-1] = int(yb)
			self.ycList[0:int(self.acorr.get_xlim()[1])-1] = self.ycList[1:int(self.acorr.get_xlim()[1])]
			self.ycList[int(self.acorr.get_xlim()[1])-1] = int(yc)



		self.line1.set_xdata(np.arange(0,len(self.yList)))
		self.line1.set_ydata((self.yList))

		self.line2.set_xdata(np.arange(0,len(self.ybList)))
		self.line2.set_ydata((self.ybList))

		self.line3.set_xdata(np.arange(0,len(self.ycList)))
		self.line3.set_ydata((self.ycList))


		self.canvascorr.draw()
		self.canvastensao.draw()
		self.canvastemperatura.draw()



	
	def updateBat(self,dados,falhas=0):
		
		#Lê os valores do dicionário que contém os dados
		vtemp = dados['values']['TE_202']
		vcorr = dados['values']['IE_201']
		vten = dados['values']['EE_202']


		#Destrói os Label antigos dos valores
		self.temp.destroy()
		self.corr.destroy()
		self.ten.destroy()

		

		#Cria os novos labels com os novos valores
		if 'TE_202' not in falhas:
			self.temp = Label(self,text=vtemp,font=("Arial", 14))
			self.temp.place(x=400,y=95)
		else:
			self.temp = Label(self,text=vtemp,font=("Arial", 14),foreground='#f00')
			self.temp.place(x=400,y=95)
		if 'IE_201' not in falhas:
			self.corr = Label(self,text=vcorr,font=("Arial", 14))
			self.corr.place(x=580,y=95)
		else:
			self.corr = Label(self,text=vcorr,font=("Arial", 14),foreground='#f00')
			self.corr.place(x=580,y=95)
		if 'EE_202' not in falhas:
			self.ten = Label(self,text=vten,font=("Arial", 14))
			self.ten.place(x=760,y=95)
		else:
			self.ten = Label(self,text=vten,font=("Arial", 14),foreground='#f00')
			self.ten.place(x=760,y=95)
		try:
			self.falha.config(text = ",".join(falhas),fg='#f00')
		except:
			self.falha.config(text = '------')
	


		




