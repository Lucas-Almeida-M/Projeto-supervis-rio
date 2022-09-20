from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import Button as SButton
from tkinter import Label as SLabel
from turtle import color
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
from PIL import ImageTk, Image
style.use("dark_background")


class Turbina ( Frame ):



	def __init__(self,configs,modbus_addrs,parent, controller):
		Frame.__init__(self, parent)


		self.controller = controller
		

		self.xList = []
		self.yList = []
		self.ybList = []
		self.ycList = []
		self.ydList = []
		self.yeList = []
		self.yfList = []
		self.ygList = []
		self.yhList = []
		self.yiList = []

		
		self.status = LabelFrame(self,text='STATUS',border=15,padding=20)
		self.status.grid(row=0,column=0,columnspan=2,rowspan=4,padx=10,pady=5,sticky="n")



		lturb = Label(self.status,text='Turbina:',font=("Arial", 14),padding=(0,0,0,10))
		lturb.grid(row=0,column=0,padx=35)
		self.turb = SLabel(self.status,text='Desligada',font=("Arial", 14),fg='#f00')
		self.turb.grid(row=1,column=0)
		s1 = Separator(self.status, orient=HORIZONTAL)
		s1.grid(row=2,column=0, sticky="ew",pady=30)
		lfalha = Label(self.status,text='Falhas:',font=("Arial", 14),padding=(0,0,0,10))
		lfalha.grid(row=3,column=0)
		self.falha = SLabel(self.status,text='---------',font=("Arial", 10),fg='#0f0')
		self.falha.grid(row=4,column=0)

		self.fdados = LabelFrame(self,text='Dados',border=15,padding=20)
		self.fdados.grid(row=0,column=2,columnspan=2,rowspan=6,padx=10,pady=5,sticky="n")

		lvazaocomb = Label(self.fdados,text='Vazão de Combustível',font=("Arial", 13),padding=(0,0,0,20))
		lvazaocomb.grid(row=0,column=0,padx=20,sticky='w')
		lvazaoar = Label(self.fdados,text='Vazão de Ar',font=("Arial", 13),padding=(0,0,0,20))
		lvazaoar.grid(row=1,column=0,padx=20,sticky='w')
		lpressaocomb = Label(self.fdados,text='Pressão do Combustível',font=("Arial", 13),padding=(0,0,0,20))
		lpressaocomb.grid(row=2,column=0,padx=20,sticky='w')
		lpressaocompr = Label(self.fdados,text='Pressão na Saída do Compressor',font=("Arial", 13),padding=(0,0,0,20))
		lpressaocompr.grid(row=3,column=0,padx=20,sticky='w')
		lpressaoexast = Label(self.fdados,text='Pressão na Chaminé',font=("Arial", 13),padding=(0,0,0,20))
		lpressaoexast.grid(row=4,column=0,padx=20,sticky='w')
		lpressaomani = Label(self.fdados,text='Pressão no Manifold',font=("Arial", 13),padding=(0,0,0,20))
		lpressaomani.grid(row=5,column=0,padx=20,sticky='w')
		ltempcomb = Label(self.fdados,text='Temperatura do Combustível',font=("Arial", 13),padding=(0,0,0,20))
		ltempcomb.grid(row=6,column=0,padx=20,sticky='w')
		ltempexaust = Label(self.fdados,text='Temperatura na Chaminé',font=("Arial", 13),padding=(0,0,0,20))
		ltempexaust.grid(row=7,column=0,padx=20,sticky='w')
		ltempcompr = Label(self.fdados,text='Temperatura na Saída do Compressor',font=("Arial", 13),padding=(0,0,0,0))
		ltempcompr.grid(row=8,column=0,padx=20,sticky='w')

		svazaocomb = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		svazaocomb.grid(row=0,column=1,padx=20)
		svazaoar = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		svazaoar.grid(row=1,column=1,padx=20)
		spressaocomb = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		spressaocomb.grid(row=2,column=1,padx=20)
		spressaocompr = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		spressaocompr.grid(row=3,column=1,padx=20)
		spressaoexast = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		spressaoexast.grid(row=4,column=1,padx=20)
		spressaomani = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		spressaomani.grid(row=5,column=1,padx=20)
		stempcomb = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		stempcomb.grid(row=6,column=1,padx=20)
		stempexaust = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,20))
		stempexaust.grid(row=7,column=1,padx=20)
		stempcompr = Label(self.fdados,text=':',font=("Arial", 13, 'bold'),padding=(0,0,0,0))
		stempcompr.grid(row=8,column=1,padx=20)


		self.vazaocomb = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.vazaocomb.grid(row=0,column=2,padx=30,sticky='ew')
		self.vazaoar = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.vazaoar.grid(row=1,column=2,padx=30)
		self.pressaocomb = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.pressaocomb.grid(row=2,column=2,padx=20)
		self.pressaocompr = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.pressaocompr.grid(row=3,column=2,padx=20)
		self.pressaoexast = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.pressaoexast.grid(row=4,column=2,padx=20)
		self.pressaomani = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.pressaomani.grid(row=5,column=2,padx=20)
		self.tempcomb = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.tempcomb.grid(row=6,column=2,padx=20)
		self.tempexaust = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,20))
		self.tempexaust.grid(row=7,column=2,padx=20)
		self.tempcompr = Label(self.fdados,text='-------',width=7,font=("Arial", 13),padding=(0,0,0,0))
		self.tempcompr.grid(row=8,column=2,padx=20)

		uvazaocomb = Label(self.fdados,text='mL/h',font=("Arial", 13),padding=(0,0,0,20))
		uvazaocomb.grid(row=0,column=3,sticky='w')
		uvazaoar = Label(self.fdados,text='---',font=("Arial", 13),padding=(0,0,0,20))
		uvazaoar.grid(row=1,column=3,sticky='w')
		upressaocomb = Label(self.fdados,text='Bar',font=("Arial", 13),padding=(0,0,0,20))
		upressaocomb.grid(row=2,column=3,sticky='w')
		upressaocompr = Label(self.fdados,text='Bar',font=("Arial", 13),padding=(0,0,0,20))
		upressaocompr.grid(row=3,column=3,sticky='w')
		upressaoexast = Label(self.fdados,text='Bar',font=("Arial", 13),padding=(0,0,0,20))
		upressaoexast.grid(row=4,column=3,sticky='w')
		upressaomani = Label(self.fdados,text='Bar',font=("Arial", 13),padding=(0,0,0,20))
		upressaomani.grid(row=5,column=3,sticky='w')
		utempcomb = Label(self.fdados,text='°C',font=("Arial", 13),padding=(0,0,0,20))
		utempcomb.grid(row=6,column=3,sticky='w')
		utempexaust = Label(self.fdados,text='°C',font=("Arial", 13),padding=(0,0,0,20))
		utempexaust.grid(row=7,column=3,sticky='w')
		utempcompr = Label(self.fdados,text='°C',font=("Arial", 13),padding=(0,0,0,0))
		utempcompr.grid(row=8,column=3,sticky='w')


		self.fsolenoides = LabelFrame(self,text='SOLENOIDES',border=5,padding=10)
		self.fsolenoides.grid(row=6,column=2,columnspan=2,rowspan=2,padx=10,pady=5,sticky="n")

		lsol1 = Label(self.fsolenoides,text='Solenoide de Dreno	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol1.grid(row=0,column=0,padx=10,sticky='w')

		lsol2 = Label(self.fsolenoides,text='Solenoide Prime		:',font=("Arial", 13),padding=(0,0,0,20))
		lsol2.grid(row=1,column=0,padx=10,sticky='w')

		lsol3 = Label(self.fsolenoides,text='Solenoide Saída Compressor	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol3.grid(row=2,column=0,padx=10,sticky='w')

		lsol4 = Label(self.fsolenoides,text='Solenoide Entrada Manifold	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol4.grid(row=3,column=0,padx=10,sticky='w')

		lsol5 = Label(self.fsolenoides,text='Solenoide Bico Injetor 1	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol5.grid(row=0,column=2,padx=10,sticky='w')

		lsol6 = Label(self.fsolenoides,text='Solenoide Bico Injetor 2	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol6.grid(row=1,column=2,padx=10,sticky='w')

		lsol7 = Label(self.fsolenoides,text='Solenoide Ar Manifold	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol7.grid(row=2,column=2,padx=10,sticky='w')

		lsol8 = Label(self.fsolenoides,text='Solenoide de Dreno	:',font=("Arial", 13),padding=(0,0,0,20))
		lsol8.grid(row=3,column=2,padx=10,sticky='w')

		estadoimg = (Image.open("img/des.png"))
		new_image= ImageTk.PhotoImage(estadoimg)
		self.new_image = new_image
		
		self.estado1 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado1.grid(row=0,column=1,padx=10,sticky='ns')
		self.estado1.create_image(15, 15, image=new_image,anchor='se')

		self.estado2 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado2.grid(row=1,column=1,padx=10,sticky='ns')
		self.estado2.create_image(15, 15, image=new_image,anchor='se')

		self.estado3 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado3.grid(row=2,column=1,padx=10,sticky='ns')
		self.estado3.create_image(15, 15, image=new_image,anchor='se')

		self.estado4 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado4.grid(row=3,column=1,padx=10,sticky='ns')
		self.estado4.create_image(15, 15, image=new_image,anchor='se')

		self.estado5 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado5.grid(row=0,column=3,padx=10,sticky='ns')
		self.estado5.create_image(15, 15, image=new_image,anchor='se')

		self.estado6 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado6.grid(row=1,column=3,padx=10,sticky='ns')
		self.estado6.create_image(15, 15, image=new_image,anchor='se')

		self.estado7 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado7.grid(row=2,column=3,padx=10,sticky='ns')
		self.estado7.create_image(15, 15, image=new_image,anchor='se')

		self.estado8 = Canvas(self.fsolenoides, width=15, height=15)
		self.estado8.grid(row=3,column=3,padx=10,sticky='ns')
		self.estado8.create_image(15, 15, image=new_image,anchor='se')



		self.fmisc = LabelFrame(self,text='',border=5,padding=10)
		self.fmisc.grid(row=6,column=0,columnspan=2,rowspan=2,padx=10,pady=5,sticky="n")

		lmisc1 = Label(self.fmisc,text='Nível Alto T. Dreno	  :',font=("Arial", 13),padding=(0,0,0,20))
		lmisc1.grid(row=0,column=0,padx=10,sticky='w')

		lmisc2 = Label(self.fmisc,text='Nível Baixo T. Dreno :',font=("Arial", 13),padding=(0,0,0,20))
		lmisc2.grid(row=1,column=0,padx=10,sticky='w')

		lmisc3 = Label(self.fmisc,text='Nível Baixo T. Comb.:',font=("Arial", 13),padding=(0,0,0,20))
		lmisc3.grid(row=2,column=0,padx=10,sticky='w')

		lmisc4 = Label(self.fmisc,text='Vela de Ignição	  :',font=("Arial", 13),padding=(0,0,0,20))
		lmisc4.grid(row=3,column=0,padx=10,sticky='w')

		self.misc1 = Canvas(self.fmisc, width=15, height=15)
		self.misc1.grid(row=0,column=1,padx=10,sticky='ns')
		self.misc1.create_image(15, 15, image=new_image,anchor='se')

		self.misc2 = Canvas(self.fmisc, width=15, height=15)
		self.misc2.grid(row=1,column=1,padx=10,sticky='ns')
		self.misc2.create_image(15, 15, image=new_image,anchor='se')

		self.misc3 = Canvas(self.fmisc, width=15, height=15)
		self.misc3.grid(row=2,column=1,padx=10,sticky='ns')
		self.misc3.create_image(15, 15, image=new_image,anchor='se')

		self.misc4 = Canvas(self.fmisc, width=15, height=15)
		self.misc4.grid(row=3,column=1,padx=10,sticky='ns')
		self.misc4.create_image(15, 15, image=new_image,anchor='se')



	
		bhome = Button(self, text="HOME", command=lambda: controller.show_frame("PageOne"))
		bhome.grid(row=4,column=0,sticky='we',padx=10,pady=50)

		bconfig = Button(self, text="Configurações", command=self.controller.frames['PageOne'].configuracoes)
		bconfig.grid(row=5,column=0,sticky='nwe',padx=10)

		bexpdados = Button(self, text="Exportar Dados", command=self.controller.frames['PageOne'].exportar)
		bexpdados.grid(row=5,column=1,sticky='nwe',padx=10)

		bhistdados = Button(self, text="Histórico de Dados", command=self.controller.frames['PageOne'].historico)
		bhistdados.grid(row=4,column=1,sticky='we',padx=10)
		
		
		self.fvazao = Figure(figsize=(5, 2.3))
		self.avazao = self.fvazao.add_subplot(111)
		self.avazao.set_xlim(0,configs['txlim'])
		self.avazao.set_ylim(0,configs['tvylim'])
		self.avazao.set_ylabel("Vazão [mL/h]")
		self.line1 = self.avazao.plot([],[],label='Vazão de Combustível',color="blue")[0]
		self.line2 = self.avazao.plot([],[],label='Vazão de Ar',color="red")[0]
		self.avazao.legend(handles=[self.line1, self.line2],loc='upper right',fontsize=8)

		self.canvasvazao = FigureCanvasTkAgg(self.fvazao,master=self)
		self.canvasvazao.get_tk_widget().grid(row=0,column=8,rowspan=3)
		self.canvasvazao.draw()




		self.fpressao = Figure(figsize=(5, 2.3))
		self.apressao = self.fpressao.add_subplot(111)
		self.apressao.set_xlim(0,configs['txlim'])
		self.apressao.set_ylim(0,configs['tpylim'])
		self.apressao.set_ylabel("Pressão [Bar]")
		self.line3 = self.apressao.plot([],[],label='Pressão 1',color="blue")[0]
		self.line4 = self.apressao.plot([],[],label='Pressão 2',color="red")[0]
		self.line5 = self.apressao.plot([],[],label='Pressão 3',color="yellow")[0]
		self.line6 = self.apressao.plot([],[],label='Pressão 4',color="green")[0]
		self.apressao.legend(handles=[self.line3, self.line4,self.line5, self.line6],loc='upper right',fontsize=8)

		self.canvaspressao = FigureCanvasTkAgg(self.fpressao,master=self)
		self.canvaspressao.get_tk_widget().grid(row=3,column=8,rowspan=3)
		self.canvaspressao.draw()




		self.ftemperatura = Figure(figsize=(5, 2.4))
		self.atemperatura = self.ftemperatura.add_subplot(111)
		self.atemperatura.set_xlim(0,configs['txlim'])
		self.atemperatura.set_ylim(0,configs['ttemplim'])
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line7 = self.atemperatura.plot([],[],label='Temperatura 1',color="blue")[0]
		self.line8 = self.atemperatura.plot([],[],label='Temperatura 2',color="red")[0]
		self.line9 = self.atemperatura.plot([],[],label='Temperatura 3',color="yellow")[0]
		self.atemperatura.legend(handles=[self.line7, self.line8,self.line9],loc='upper right',fontsize=8)

		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=6,column=8,rowspan=3)
		self.canvastemperatura.draw()


		# toolbar = NavigationToolbar2TkAgg(canvas)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


		# self.after(100,self.animate)

	def set_t(self,limcy,limty,limtempy,limx):

		self.avazao.clear()
		self.avazao.set_ylim(0,limcy)
		self.avazao.set_xlim(0,limx)
		self.avazao.set_ylabel("Vazão [mL/h]")
		self.line1 = self.avazao.plot([],[],label='Vazão de Combustível',color="blue")[0]
		self.line2 = self.avazao.plot([],[],label='Vazão de Ar',color="red")[0]
		self.avazao.legend(handles=[self.line1, self.line2],loc='upper right',fontsize=8)

		self.canvasvazao.get_tk_widget().delete()
		self.canvasvazao = FigureCanvasTkAgg(self.fvazao,master=self)
		self.canvasvazao.get_tk_widget().grid(row=0,column=8,rowspan=3)
		self.canvasvazao.draw()



		self.apressao.clear()
		self.apressao.set_xlim(0,limx)
		self.apressao.set_ylim(0,limty)
		self.apressao.set_ylabel("Pressão [Bar]")
		self.line3 = self.apressao.plot([],[],label='Pressão 1',color="blue")[0]
		self.line4 = self.apressao.plot([],[],label='Pressão 2',color="red")[0]
		self.line5 = self.apressao.plot([],[],label='Pressão 3',color="yellow")[0]
		self.line6 = self.apressao.plot([],[],label='Pressão 4',color="green")[0]
		self.apressao.legend(handles=[self.line3, self.line4,self.line5, self.line6],loc='upper right',fontsize=8)

		self.canvaspressao.get_tk_widget().delete()
		self.canvaspressao = FigureCanvasTkAgg(self.fpressao,master=self)
		self.canvaspressao.get_tk_widget().grid(row=3,column=8,rowspan=3)
		self.canvaspressao.draw()



		self.atemperatura.clear()
		self.atemperatura.set_xlim(0,limx)
		self.atemperatura.set_ylim(0,limtempy)
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line7 = self.atemperatura.plot([],[],label='Temperatura 1',color="blue")[0]
		self.line8 = self.atemperatura.plot([],[],label='Temperatura 2',color="red")[0]
		self.line9 = self.atemperatura.plot([],[],label='Temperatura 3',color="yellow")[0]
		self.atemperatura.legend(handles=[self.line7, self.line8,self.line9],loc='upper right',fontsize=8)

		self.canvastemperatura.get_tk_widget().delete()
		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=6,column=8,rowspan=3)
		self.canvastemperatura.draw()


	def animate(self, dados):

		try:
			y = dados['values']['FT_001']
			yb = dados['values']['FT_002']
			yc = dados['values']['PT_001']
			yd = dados['values']['PT_002']
			ye = dados['values']['PT_003']
			yf = dados['values']['PT_004']
			yg = dados['values']['TT_001']
			yh = dados['values']['TT_002']
			yi = dados['values']['TT_003']
		except:
			y = 0
			yb = 0
			yc = 0
			yd = 0
			ye = 0
			yf = 0
			yg = 0
			yh = 0
			yi = 0


		if(len(self.yList)<100):
			self.yList.append(y)
			self.ybList.append(yb)
			self.ycList.append(yc)
			self.ydList.append(yd)
			self.yeList.append(ye)
			self.yfList.append(yf)
			self.ygList.append(yg)
			self.yhList.append(yh)
			self.yiList.append(yi)
		elif(len(self.yList)>=100):
			self.yList[0:99] = self.yList[1:100]
			self.yList[99] = int(y)
			self.ybList[0:99] = self.ybList[1:100]
			self.ybList[99] = int(yb)
			self.ycList[0:99] = self.ycList[1:100]
			self.ycList[99] = int(yc)
			self.ydList[0:99] = self.ydList[1:100]
			self.ydList[99] = int(yd)
			self.yeList[0:99] = self.yeList[1:100]
			self.yeList[99] = int(ye)
			self.yfList[0:99] = self.yfList[1:100]
			self.yfList[99] = int(yf)
			self.ygList[0:99] = self.ygList[1:100]
			self.ygList[99] = int(yg)
			self.yhList[0:99] = self.yhList[1:100]
			self.yhList[99] = int(yh)
			self.yiList[0:99] = self.yiList[1:100]
			self.yiList[99] = int(yi)

		self.line1.set_xdata(np.arange(0,len(self.yList)))
		self.line1.set_ydata((self.yList))
		self.line2.set_xdata(np.arange(0,len(self.ybList)))
		self.line2.set_ydata((self.ybList))


		self.line3.set_xdata(np.arange(0,len(self.ycList)))
		self.line3.set_ydata((self.ycList))
		self.line4.set_xdata(np.arange(0,len(self.ydList)))
		self.line4.set_ydata((self.ydList))
		self.line5.set_xdata(np.arange(0,len(self.yeList)))
		self.line5.set_ydata((self.yeList))
		self.line6.set_xdata(np.arange(0,len(self.yfList)))
		self.line6.set_ydata((self.yfList))

		self.line7.set_xdata(np.arange(0,len(self.ygList)))
		self.line7.set_ydata((self.ygList))
		self.line8.set_xdata(np.arange(0,len(self.yhList)))
		self.line8.set_ydata((self.yhList))
		self.line9.set_xdata(np.arange(0,len(self.yiList)))
		self.line9.set_ydata((self.yiList))

		self.canvasvazao.draw()
		self.canvaspressao.draw()
		self.canvastemperatura.draw()
		
		# self.after(100,self.animate)
		# a.clear()
		# a.plot(xList, yList)
	
	def updateTurb(self,dados,falhas=[0]):


		vazaocomb1 = dados['values']['FT_001']
		vazaoar1 = dados['values']['FT_002']
		pressaocomb1 = dados['values']['PT_001']
		pressaocompr1 = dados['values']['PT_002']
		pressaoexast1 = dados['values']['PT_003']
		pressaomani1 = dados['values']['PT_004']
		tempcomb1 = dados['values']['TT_001']
		tempexaust1 = dados['values']['TT_002']
		tempcompr1 = dados['values']['TT_003']

		self.vazaocomb.destroy()
		self.vazaoar.destroy()
		self.pressaocomb.destroy()
		self.pressaocompr.destroy()
		self.pressaoexast.destroy()
		self.pressaomani.destroy()
		self.tempcomb.destroy()
		self.tempexaust.destroy()
		self.tempcompr.destroy()

		
		if 'FT_001' not in falhas:
			self.vazaocomb = Label(self.fdados,text=vazaocomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.vazaocomb.grid(row=0,column=2,padx=30,sticky='ew')
		else:
			self.vazaocomb = Label(self.fdados,text=vazaocomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.vazaocomb.grid(row=0,column=2,padx=30,sticky='ew')
		if 'FT_002' not in falhas:
			self.vazaoar = Label(self.fdados,text=vazaoar1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.vazaoar.grid(row=1,column=2,padx=30,sticky='ew')
		else:
			self.vazaoar = Label(self.fdados,text=vazaoar1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.vazaoar.grid(row=1,column=2,padx=30,sticky='ew')
		if 'PT_001' not in falhas:
			self.pressaocomb = Label(self.fdados,text=pressaocomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.pressaocomb.grid(row=2,column=2,padx=30,sticky='ew')
		else:
			self.pressaocomb = Label(self.fdados,text=pressaocomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.pressaocomb.grid(row=2,column=2,padx=30,sticky='ew')
		if 'PT_002' not in falhas:	
			self.pressaocompr = Label(self.fdados,text=pressaocompr1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.pressaocompr.grid(row=3,column=2,padx=30,sticky='ew')
		else:
			self.pressaocompr = Label(self.fdados,text=pressaocompr1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.pressaocompr.grid(row=3,column=2,padx=30,sticky='ew')
		if 'PT_003' not in falhas:	
			self.pressaoexast = Label(self.fdados,text=pressaoexast1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.pressaoexast.grid(row=4,column=2,padx=30,sticky='ew')
		else:
			self.pressaoexast = Label(self.fdados,text=pressaoexast1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.pressaoexast.grid(row=4,column=2,padx=30,sticky='ew')
		if 'PT_004' not in falhas:
			self.pressaomani = Label(self.fdados,text=pressaomani1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.pressaomani.grid(row=5,column=2,padx=30,sticky='ew')
		else:
			self.pressaomani = Label(self.fdados,text=pressaomani1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.pressaomani.grid(row=5,column=2,padx=30,sticky='ew')
		if 'TT_001' not in falhas:
			self.tempcomb = Label(self.fdados,text=tempcomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.tempcomb.grid(row=6,column=2,padx=30,sticky='ew')
		else:
			self.tempcomb = Label(self.fdados,text=tempcomb1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.tempcomb.grid(row=6,column=2,padx=30,sticky='ew')
		if 'TT_002' not in falhas:
			self.tempexaust = Label(self.fdados,text=tempexaust1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e')
			self.tempexaust.grid(row=7,column=2,padx=30,sticky='ew')
		else:
			self.tempexaust = Label(self.fdados,text=tempexaust1,width=7,font=("Arial", 13),padding=(0,0,0,20),anchor='e',foreground='#f00')
			self.tempexaust.grid(row=7,column=2,padx=30,sticky='ew')
		if 'TT_003' not in falhas:	
			self.tempcompr = Label(self.fdados,text=tempcompr1,width=7,font=("Arial", 13),padding=(0,0,0,0),anchor='e')
			self.tempcompr.grid(row=8,column=2,padx=30,sticky='ew')
		else:
			self.tempcompr = Label(self.fdados,text=tempcompr1,width=7,font=("Arial", 13),padding=(0,0,0,0),anchor='e',foreground='#f00')
			self.tempcompr.grid(row=8,column=2,padx=30,sticky='ew')
		
		try:
			if falhas != []:
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
			else:
				self.falha.config(text = "",fg='#000000')
		except:
			pass 