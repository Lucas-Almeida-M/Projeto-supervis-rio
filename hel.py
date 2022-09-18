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


class Helice( Frame ):



	def __init__(self,configs,modbus_addrs,parent, controller):
		Frame.__init__(self, parent)


		self.controller = controller


		self.xList = []
		self.yList = []
		self.ybList = []
		self.ycList = []
		self.ydList = []


		
		self.status = LabelFrame(self,text='STATUS',border=40,padding=10)
		self.status.grid(row=0,column=0,columnspan=2,rowspan=4,padx=10,pady=5,sticky="nwe")



		lturb = Label(self.status,text='Motor:',font=("Arial", 14),padding=(0,0,30,10))
		lturb.grid(row=0,column=0,rowspan=2,padx=35,sticky='we')
		self.turb = SLabel(self.status,text='Desligado',font=("Arial", 14),fg='#f00')
		self.turb.grid(row=1,column=0)
		s1 = Separator(self.status, orient=HORIZONTAL)
		s1.grid(row=2,column=0, sticky="ew",pady=30)
		lfalha = Label(self.status,text='Falhas:',font=("Arial", 14),padding=(0,0,0,10))
		lfalha.grid(row=3,column=0)
		self.falha = SLabel(self.status,text='---------',font=("Arial", 14),fg='#0f0')
		self.falha.grid(row=4,column=0)


		lhel = Canvas(self, width=600, height=531)
		lhel.grid(row=0,column=2,columnspan=4,rowspan=4,padx=10,pady=45)
		helimg = (Image.open("img/mot_hel.png"))
		resized_image= helimg.resize((600,531), Image.ANTIALIAS)
		new_image= ImageTk.PhotoImage(resized_image)
		self.new_image = new_image
		lhel.create_image(600, 531, image=new_image,anchor='se')



		bhome = Button(self, text="HOME", command=lambda: controller.show_frame("PageOne"))
		bhome.grid(row=2,column=0,sticky='we',padx=10,pady=50)

		bconfig = Button(self, text="Configurações", command=self.controller.frames['PageOne'].configuracoes)
		bconfig.grid(row=3,column=0,sticky='nwe',padx=10)

		bexpdados = Button(self, text="Exportar Dados", command=self.controller.frames['PageOne'].exportar)
		bexpdados.grid(row=3,column=1,sticky='nwe',padx=10)

		bhistdados = Button(self, text="Histórico de Dados", command=self.controller.frames['PageOne'].historico)
		bhistdados.grid(row=2,column=1,sticky='we',padx=10)




		self.ftorque = Figure(figsize=(5, 2.3))
		self.atorque = self.ftorque.add_subplot(111)
		self.atorque.set_xlim(0,configs['hxlim'])
		self.atorque.set_ylim(0,configs['htorqueylim'])
		self.atorque.set_ylabel("Torque [N.m]")
		self.line1 = self.atorque.plot([],[],color="blue")[0]
		# self.atorque.legend(handles=[self.line1],loc='upper right')

		self.canvastorque = FigureCanvasTkAgg(self.ftorque,master=self)
		self.canvastorque.get_tk_widget().grid(row=0,column=8)
		self.canvastorque.draw()



		self.femp = Figure(figsize=(5, 2.3))
		self.aemp = self.femp.add_subplot(111)
		self.aemp.set_xlim(0,configs['hxlim'])
		self.aemp.set_ylim(0,configs['hempylim'])
		self.aemp.set_ylabel("Empuxo [N]")
		self.line2 = self.aemp.plot([],[],color="blue")[0]
		# self.aemp.legend(handles=[self.line2],loc='upper right')

		self.canvasemp = FigureCanvasTkAgg(self.femp,master=self)
		self.canvasemp.get_tk_widget().grid(row=1,column=8,rowspan=2)
		self.canvasemp.draw()



		self.ftemperatura = Figure(figsize=(5, 2.4))
		self.atemperatura = self.ftemperatura.add_subplot(111)
		self.atemperatura.set_xlim(0,configs['hxlim'])
		self.atemperatura.set_ylim(0,configs['htemplim'])
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line3 = self.atemperatura.plot([],[],label='Temperatura 1',color="blue")[0]
		self.line4 = self.atemperatura.plot([],[],label='Temperatura 2',color="red")[0]
		self.atemperatura.legend(handles=[self.line3, self.line4],loc='upper right',fontsize=8)

		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=3,column=8)
		self.canvastemperatura.draw()



		#Frame que ficam dados de Torque e Empuxo
		self.fdad = LabelFrame(self,border=15,padding=10)
		self.fdad.place(x=490,y=530)

		#Label do Torque
		ltorque = Label(self.fdad,text='Torque do Conjunto',font=("Arial", 14))
		ltorque.grid(row=0,column=0,sticky=W)
		septorque = Label(self.fdad,text=':',font=("Arial bold", 14))
		septorque.grid(row=0,column=1,sticky=W,padx=15)
		self.torque = Label(self.fdad,text='  ----',font=("Arial", 14))
		self.torque.grid(row=0,column=2,padx=30,sticky=W)
		utorque = Label(self.fdad,text='N.m',font=("Arial", 14))
		utorque.grid(row=0,column=3,sticky=W)


		#Label do Empuxo
		lemp = Label(self.fdad,text='Empuxo do Conjunto',font=("Arial", 14))
		lemp.grid(row=1,column=0,sticky=W)
		sepemp = Label(self.fdad,text=':',font=("Arial bold", 14))
		sepemp.grid(row=1,column=1,sticky=W,padx=15)
		self.emp = Label(self.fdad,text='  ----',font=("Arial", 14))
		self.emp.grid(row=1,column=2,padx=30,sticky=W)
		uemp = Label(self.fdad,text='N',font=("Arial", 14))
		uemp.grid(row=1,column=3,sticky=W)


		#Label das Temperaturas do gerador e motor
		self.tempmot = Label(self,text='  ----',font=("Arial", 14))
		self.tempmot.place(x=390,y=240)
		ltempmot = Label(self,text='°C',font=("Arial", 14))
		ltempmot.place(x=429,y=240)
		self.tempger = Label(self,text='  ----',font=("Arial", 14))
		self.tempger.place(x=570,y=120)
		ltempger = Label(self,text='°C',font=("Arial", 14))
		ltempger.place(x=609,y=120)
	  

	def set_h(self,limcy,limty,limtempy,limx):

		self.atorque.clear()
		self.atorque.set_ylim(0,limcy)
		self.atorque.set_xlim(0,limx)
		
		self.atorque.set_ylabel("Torque [N.m]")
		self.line1 = self.atorque.plot([],[],color="blue")[0]
		# self.atorque.legend(handles=[self.line1],loc='upper right')

		self.canvastorque.get_tk_widget().delete()
		self.canvastorque = FigureCanvasTkAgg(self.ftorque,master=self)
		self.canvastorque.get_tk_widget().grid(row=0,column=8)
		self.canvastorque.draw()



		self.aemp.clear()
		self.aemp.set_xlim(0,limx)
		self.aemp.set_ylim(0,limty)
		self.aemp.set_ylabel("Empuxo [N]")
		self.line2 = self.aemp.plot([],[],color="blue")[0]
		# self.aemp.legend(handles=[self.line2],loc='upper right')

		self.canvasemp.get_tk_widget().delete()
		self.canvasemp = FigureCanvasTkAgg(self.femp,master=self)
		self.canvasemp.get_tk_widget().grid(row=1,column=8,rowspan=2)
		self.canvasemp.draw()



		self.atemperatura.clear()
		self.atemperatura.set_xlim(0,limx)
		self.atemperatura.set_ylim(0,limtempy)
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line3 = self.atemperatura.plot([],[],label='Temperatura C1',color="blue")[0]
		self.line4 = self.atemperatura.plot([],[],label='Temperatura C3',color="red")[0]
		self.atemperatura.legend(handles=[self.line3, self.line4],loc='upper right')

		self.canvastemperatura.get_tk_widget().delete()
		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=3,column=8)
		self.canvastemperatura.draw()



		

		




	def animate(self, dados):

		try:
			y = dados['values']['WT_402'] 
			yb = dados['values']['WT_401'] 
			yc = dados['values']['TE_401'] 
			yd = dados['values']['TE_402'] 

		except:
			y = 0
			yb = 0
			yc = 0
			yd = 0


		if(len(self.yList)<int(self.atorque.get_xlim()[1])):
			self.yList.append(y)
			self.ybList.append(yb)
			self.ycList.append(yc)
			self.ydList.append(yd)


		elif(len(self.yList)>=int(self.atorque.get_xlim()[1])):
			self.yList[0:int(self.atorque.get_xlim()[1])-1] = self.yList[1:int(self.atorque.get_xlim()[1])]
			self.yList[int(self.atorque.get_xlim()[1])-1] = int(y)
			self.ybList[0:int(self.atorque.get_xlim()[1])-1] = self.ybList[1:int(self.atorque.get_xlim()[1])]
			self.ybList[int(self.atorque.get_xlim()[1])-1] = int(yb)
			self.ycList[0:int(self.atorque.get_xlim()[1])-1] = self.ycList[1:int(self.atorque.get_xlim()[1])]
			self.ycList[int(self.atorque.get_xlim()[1])-1] = int(yc)
			self.ydList[0:int(self.atorque.get_xlim()[1])-1] = self.ydList[1:int(self.atorque.get_xlim()[1])]
			self.ydList[int(self.atorque.get_xlim()[1])-1] = int(yd)



		self.line1.set_xdata(np.arange(0,len(self.yList)))
		self.line1.set_ydata((self.yList))


		self.line2.set_xdata(np.arange(0,len(self.ybList)))
		self.line2.set_ydata((self.ybList))



		self.line3.set_xdata(np.arange(0,len(self.ycList)))
		self.line3.set_ydata((self.ycList))
		self.line4.set_xdata(np.arange(0,len(self.ydList)))
		self.line4.set_ydata((self.ydList))



		self.canvastorque.draw()
		self.canvasemp.draw()
		self.canvastemperatura.draw()
		
		# self.after(100,self.animate)
		# a.clear()
		# a.plot(xList, yList)


	
	def updateHel(self,dados,falhas=0):


		#Lê os valores do dicionário que contém os dados
		torque = dados['values']['WT_402']
		emp = dados['values']['WT_401']
		tempmot = dados['values']['TE_401']
		tempger = dados['values']['TE_402']

 

		#Destrói os Label antigos dos valores
		self.torque.destroy()
		self.emp.destroy()
		self.tempmot.destroy()
		self.tempger.destroy()

	

		#Cria os novos labels com os novos valores
		if 'WT_402' not in falhas:
			self.torque = Label(self.fdad,text=torque,font=("Arial", 14))
			self.torque.grid(row=0,column=2,padx=30,sticky=W)
		else:
			self.torque = Label(self.fdad,text=torque,font=("Arial", 14),foreground = '#f00')
			self.torque.grid(row=0,column=2,padx=30,sticky=W)
		if 'WT_401' not in falhas:
			self.emp = Label(self.fdad,text=emp,font=("Arial", 14))
			self.emp.grid(row=1,column=2,padx=30,sticky=W)
		else:
			self.emp = Label(self.fdad,text=emp,font=("Arial", 14),foreground = '#f00')
			self.emp.grid(row=1,column=2,padx=30,sticky=W)
		if 'TE_401' not in falhas:
			self.tempmot = Label(self,text=tempmot,font=("Arial", 14))
			self.tempmot.place(x=390,y=240)
		else:
			self.tempmot = Label(self,text=tempmot,font=("Arial", 14),foreground = '#f00')
			self.tempmot.place(x=390,y=240)
		if 'TE_402' not in falhas:
			self.tempger = Label(self,text=tempger,font=("Arial", 14))
			self.tempger.place(x=570,y=120)
		else:
			self.tempger = Label(self,text=tempger,font=("Arial", 14),foreground = '#f00')
			self.tempger.place(x=570,y=120)
		try:
			if falhas[0] != 0:
				texto = []
				for n in range(len(falhas)):
					if (n != 0 and n%3 == 0):
						texto.append("\n")
						texto.append(falhas[n])
						texto.append(',')
					elif ((len(falhas)%3 != 0) and n == (len(falhas)-1)):
						texto.append(falhas[n])
					elif len(falhas) == 3 and n == 2:
						texto.append(falhas[n])
					else: 
						texto.append(falhas[n])
						texto.append(',')
				texto_falhas = ''.join(texto)
				self.falha.config(text = "".join(texto_falhas),fg='#f00')
		except:
			 pass