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


class Conversores( Frame ):



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


		
		self.status = LabelFrame(self,text='STATUS',border=40,padding=10)
		self.status.grid(row=0,column=0,columnspan=2,rowspan=2,padx=10,pady=5,sticky="nw")

		lturb = Label(self.status,text='Conversores:',font=("Arial", 14),padding=(0,0,0,10))
		lturb.grid(row=0,column=0,padx=35)
		self.turb = SLabel(self.status,text='Desligados',font=("Arial", 14),fg='#f00')
		self.turb.grid(row=1,column=0)
		s1 = Separator(self.status, orient=HORIZONTAL)
		s1.grid(row=2,column=0, sticky="ew",pady=30)
		lfalha = Label(self.status,text='Falhas:',font=("Arial", 14),padding=(0,0,0,10))
		lfalha.grid(row=3,column=0)
		self.falha = SLabel(self.status,text='---------',font=("Arial", 14),fg='#0f0')
		self.falha.grid(row=4,column=0)



		bhome = Button(self, text="HOME", command=lambda: controller.show_frame("PageOne"))
		bhome.grid(row=2,column=0,sticky='we',padx=10)

		bconfig = Button(self, text="Configurações", command=self.controller.frames['PageOne'].configuracoes)
		bconfig.grid(row=3,column=0,sticky='we',padx=10)

		bexpdados = Button(self, text="Exportar Dados", command=self.controller.frames['PageOne'].exportar)
		bexpdados.grid(row=3,column=1,sticky='we',padx=10)

		bhistdados = Button(self, text="Histórico de Dados", command=self.controller.frames['PageOne'].historico)
		bhistdados.grid(row=2,column=1,sticky='we',padx=10)


		#Cria a imagem dos conversores
		lconv = Canvas(self, width=1050, height=486)
		lconv.grid(row=0,column=2,columnspan=4,rowspan=4,padx=30,sticky='w')
		convimg = (Image.open("img/conv.png"))
		resized_image= convimg.resize((1050,486), Image.ANTIALIAS)
		new_image= ImageTk.PhotoImage(resized_image)
		self.new_image = new_image
		lconv.create_image(1050, 486, image=new_image,anchor='se')




		#Cria o gráfico de Corrente
		self.fcorr = Figure(figsize=(4.7, 2.07))
		self.acorr = self.fcorr.add_subplot(111)
		self.acorr.set_xlim(0,configs['cxlim'])
		self.acorr.set_ylim(0,configs['ccylim'])
		self.acorr.set_ylabel("Corrente [A]")
		self.line1 = self.acorr.plot([],[],label='Corrente Média C1',color="blue")[0]
		self.line2 = self.acorr.plot([],[],label='Corrente Média C3',color="red")[0]
		self.line8 = self.acorr.plot([],[],label='Corrente Bateria',color="yellow")[0]
		self.acorr.legend(handles=[self.line1, self.line2,self.line8],loc='upper right',fontsize=8)

		self.canvascorr= FigureCanvasTkAgg(self.fcorr,master=self)
		self.canvascorr.get_tk_widget().grid(row=4,column=0,rowspan=3,columnspan=3,sticky=E)
		self.canvascorr.draw()




		self.ftensao = Figure(figsize=(4.72, 2.07))
		self.atensao = self.ftensao.add_subplot(111)
		self.atensao.set_xlim(0,configs['cxlim'])
		self.atensao.set_ylim(0,configs['ctylim'])
		self.atensao.set_ylabel("Tensão [V]")
		self.line3 = self.atensao.plot([],[],label='Tensão Média C1',color="blue")[0]
		self.line4 = self.atensao.plot([],[],label='Tensão Média C3',color="red")[0]
		self.atensao.legend(handles=[self.line3, self.line4],loc='upper right',fontsize=8)

		self.canvastensao = FigureCanvasTkAgg(self.ftensao,master=self)
		self.canvastensao.get_tk_widget().grid(row=4,column=3,rowspan=3)
		self.canvastensao.draw()




		self.ftemperatura = Figure(figsize=(4.76, 2.07))
		self.atemperatura = self.ftemperatura.add_subplot(111)
		self.atemperatura.set_xlim(0,configs['cxlim'])
		self.atemperatura.set_ylim(0,configs['ctemplim'])
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.atemperatura.set_position([0.15, 0.115, 0.7, 0.77])
		self.line5 = self.atemperatura.plot([],[],label='Temperatura C1',color="blue")[0]
		self.line6 = self.atemperatura.plot([],[],label='Temperatura C3',color="red")[0]
		self.line7 = self.atemperatura.plot([],[],label='Temperatura Baterias',color="yellow")[0]
		self.atemperatura.legend(handles=[self.line5, self.line6,self.line7],loc='upper right',fontsize=8)

		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=4,column=4,rowspan=3,sticky=W)
		self.canvastemperatura.draw()




		#Labels das Tensão das fases A, B e C do conversor 1
		self.tc1a = Label(self,text='   -----',font=("Arial", 12))
		self.tc1a.place(x=458,y=30)
		self.tc1b = Label(self,text='   -----',font=("Arial", 12))
		self.tc1b.place(x=458,y=85)
		self.tc1c = Label(self,text='   -----',font=("Arial", 12))
		self.tc1c.place(x=458,y=140)

		ltc1a = Label(self,text='V',font=("Arial", 12))
		ltc1a.place(x=500,y=30)
		ltc1b = Label(self,text='V',font=("Arial", 12))
		ltc1b.place(x=500,y=85)
		ltc1c = Label(self,text='V',font=("Arial", 12))
		ltc1c.place(x=500,y=140)

		#Labels das Correntes das fases A, B e C do conversor 1
		self.cc1a = Label(self,text='  ----',font=("Arial", 12))
		self.cc1a.place(x=520,y=30)
		self.cc1b = Label(self,text='  ----',font=("Arial", 12))
		self.cc1b.place(x=520,y=85)
		self.cc1c = Label(self,text='  ----',font=("Arial", 12))
		self.cc1c.place(x=520,y=140)

		lcc1a = Label(self,text='A',font=("Arial", 12))
		lcc1a.place(x=555,y=30)
		lcc1b = Label(self,text='A',font=("Arial", 12))
		lcc1b.place(x=555,y=85)
		lcc1c = Label(self,text='A',font=("Arial", 12))
		lcc1c.place(x=555,y=140)




		#Labels das Tensão das fases A, B e C do conversor 3
		self.tc3a = Label(self,text='   -----',font=("Arial", 12),anchor='e')
		self.tc3a.place(x=1141,y=30)
		self.tc3b = Label(self,text='   -----',font=("Arial", 12))
		self.tc3b.place(x=1141,y=85)
		self.tc3c = Label(self,text='   -----',font=("Arial", 12))
		self.tc3c.place(x=1141,y=140)

		ltc3a = Label(self,text='V',font=("Arial", 12))
		ltc3a.place(x=1183,y=30)
		ltc3b = Label(self,text='V',font=("Arial", 12))
		ltc3b.place(x=1183,y=85)
		ltc3c = Label(self,text='V',font=("Arial", 12))
		ltc3c.place(x=1183,y=140)

		#Labels das Correntes das fases A, B e C do conversor 3
		self.cc3a = Label(self,text='  ----',font=("Arial", 12))
		self.cc3a.place(x=1200,y=30)
		self.cc3b = Label(self,text='  ----',font=("Arial", 12))
		self.cc3b.place(x=1200,y=85)
		self.cc3c = Label(self,text='  ----',font=("Arial", 12))
		self.cc3c.place(x=1200,y=140)

		lcc3a = Label(self,text='A',font=("Arial", 12))
		lcc3a.place(x=1232,y=30)
		lcc3b = Label(self,text='A',font=("Arial", 12))
		lcc3b.place(x=1232,y=85)
		lcc3c = Label(self,text='A',font=("Arial", 12))
		lcc3c.place(x=1232,y=140)


		#Tensão Barramento CC Conversor C2
		self.tc2 = Label(self,text='   -----',font=("Arial", 12),anchor='e')
		self.tc2.place(x=825,y=70)
		ltc2 = Label(self,text='V',font=("Arial", 12))
		ltc2.place(x=867,y=70)


		#Tensão Baterias
		self.tb = Label(self,text='   -----',font=("Arial", 14),anchor='e')
		self.tb.place(x=990,y=340)
		ltb = Label(self,text='V',font=("Arial", 14))
		ltb.place(x=1042,y=340)


		#Label da Temperatura do conversor 1
		self.tempc1 = Label(self,text='   ---',font=("Arial", 14))
		self.tempc1.place(x=645,y=165)
		ltempc1 = Label(self,text='°C',font=("Arial", 14))
		ltempc1.place(x=683,y=165)


		#Label da Temperatura do conversor 2
		self.tempc2 = Label(self,text='   ---',font=("Arial", 14))
		self.tempc2.place(x=792,y=173)
		ltempc2 = Label(self,text='°C',font=("Arial", 14))
		ltempc2.place(x=830,y=173)


		#Label da Temperatura do conversor 3
		self.tempc3 = Label(self,text='   ---',font=("Arial", 14))
		self.tempc3.place(x=1035,y=165)
		ltempc3 = Label(self,text='°C',font=("Arial", 14))
		ltempc3.place(x=1073,y=165)


		#Label da Temperatura das Baterias
		self.tempbat = Label(self,text='   ---',font=("Arial", 14))
		self.tempbat.place(x=998,y=300)
		ltempbat = Label(self,text='°C',font=("Arial", 14))
		ltempbat.place(x=1036,y=300)


		#Label da Corrente das Baterias
		self.cbat = Label(self,text='   ---',font=("Arial", 14))
		self.cbat.place(x=955,y=400)
		lcbat = Label(self,text='A',font=("Arial", 14))
		lcbat.place(x=994,y=400)


		#Label da Frequência do conversor 1
		self.freqc1 = Label(self,text='   ---',font=("Arial", 14))
		self.freqc1.place(x=575,y=165)
		lfreqc1 = Label(self,text='Hz',font=("Arial", 14))
		lfreqc1.place(x=613,y=165)


		#Label da Rotação do eixo da hélice
		self.rot = Label(self,text='   -----',font=("Arial", 13))
		self.rot.place(x=1275,y=150)
		lrot = Label(self,text='RPM',font=("Arial", 13))
		lrot.place(x=1327,y=150)


	
	def set_c(self,limcy,limty,limtempy,limx):

		self.acorr.clear()
		self.acorr.set_ylim(0,limcy)
		self.acorr.set_xlim(0,limx)
		
		self.acorr.set_ylabel("Corrente [A]")
		self.line1 = self.acorr.plot([],[],label='Corrente Média C1',color="blue")[0]
		self.line2 = self.acorr.plot([],[],label='Corrente Média C3',color="red")[0]
		self.line8 = self.acorr.plot([],[],label='Corrente Bateria',color="yellow")[0]
		self.acorr.legend(handles=[self.line1, self.line2,self.line8],loc='upper right')

		self.canvascorr.get_tk_widget().delete()
		self.canvascorr = FigureCanvasTkAgg(self.fcorr,master=self)
		self.canvascorr.get_tk_widget().grid(row=4,column=0,rowspan=3,columnspan=3)
		self.canvascorr.draw()



		self.atensao.clear()
		self.atensao.set_xlim(0,limx)
		self.atensao.set_ylim(0,limty)
		self.atensao.set_ylabel("Tensão [V]")
		self.line3 = self.atensao.plot([],[],label='Tensão Média C1',color="blue")[0]
		self.line4 = self.atensao.plot([],[],label='Tensão Média C3',color="red")[0]
		self.atensao.legend(handles=[self.line3, self.line4],loc='upper right')

		self.canvastensao.get_tk_widget().delete()
		self.canvastensao = FigureCanvasTkAgg(self.ftensao,master=self)
		self.canvastensao.get_tk_widget().grid(row=4,column=3,rowspan=3)
		self.canvastensao.draw()



		self.atemperatura.clear()
		self.atemperatura.set_xlim(0,limx)
		self.atemperatura.set_ylim(0,limtempy)
		self.atemperatura.set_ylabel("Temperatura [°C]")
		self.line5 = self.atemperatura.plot([],[],label='Temperatura C1',color="blue")[0]
		self.line6 = self.atemperatura.plot([],[],label='Temperatura C3',color="red")[0]
		self.line7 = self.atemperatura.plot([],[],label='Temperatura Baterias',color="yellow")[0]
		self.atemperatura.legend(handles=[self.line5, self.line6,self.line7],loc='upper right')

		self.canvastemperatura.get_tk_widget().delete()
		self.canvastemperatura = FigureCanvasTkAgg(self.ftemperatura,master=self)
		self.canvastemperatura.get_tk_widget().grid(row=4,column=4,rowspan=3)
		self.canvastemperatura.draw()





	def animate(self, dados):

		try:
			y = (dados['values']['IE_101'] + dados['values']['IE_102'] + dados['values']['IE_103'])/3
			yb = (dados['values']['IE_301'] + dados['values']['IE_302'] + dados['values']['IE_303'])/3
			yc = (dados['values']['EE_101'] + dados['values']['EE_102'] + dados['values']['EE_103'])/3
			yd = (dados['values']['EE_301'] + dados['values']['EE_302'] + dados['values']['EE_303'])/3
			ye = dados['values']['TE_101']
			yf = dados['values']['TE_301']
			yg = dados['values']['TE_202']
			yh = dados['values']['IE_201']
			

		except:
			y = 0
			yb = 0
			yc = 0
			yd = 0
			ye = 0
			yf = 0
			yg = 0

		if(len(self.yList)<int(self.acorr.get_xlim()[1])):
			self.yList.append(y)
			self.ybList.append(yb)
			self.ycList.append(yc)
			self.ydList.append(yd)
			self.yeList.append(ye)
			self.yfList.append(yf)
			self.ygList.append(yg)
			self.yhList.append(yh)

		elif(len(self.yList)>=int(self.acorr.get_xlim()[1])):
			self.yList[0:int(self.acorr.get_xlim()[1])-1] = self.yList[1:int(self.acorr.get_xlim()[1])]
			self.yList[int(self.acorr.get_xlim()[1])-1] = int(y)
			self.ybList[0:int(self.acorr.get_xlim()[1])-1] = self.ybList[1:int(self.acorr.get_xlim()[1])]
			self.ybList[int(self.acorr.get_xlim()[1])-1] = int(yb)
			self.ycList[0:int(self.acorr.get_xlim()[1])-1] = self.ycList[1:int(self.acorr.get_xlim()[1])]
			self.ycList[int(self.acorr.get_xlim()[1])-1] = int(yc)
			self.ydList[0:int(self.acorr.get_xlim()[1])-1] = self.ydList[1:int(self.acorr.get_xlim()[1])]
			self.ydList[int(self.acorr.get_xlim()[1])-1] = int(yd)
			self.yeList[0:int(self.acorr.get_xlim()[1])-1] = self.yeList[1:int(self.acorr.get_xlim()[1])]
			self.yeList[int(self.acorr.get_xlim()[1])-1] = int(ye)
			self.yfList[0:int(self.acorr.get_xlim()[1])-1] = self.yfList[1:int(self.acorr.get_xlim()[1])]
			self.yfList[int(self.acorr.get_xlim()[1])-1] = int(yf)
			self.ygList[0:int(self.acorr.get_xlim()[1])-1] = self.ygList[1:int(self.acorr.get_xlim()[1])]
			self.ygList[int(self.acorr.get_xlim()[1])-1] = int(yg)
			self.yhList[0:int(self.acorr.get_xlim()[1])-1] = self.yhList[1:int(self.acorr.get_xlim()[1])]
			self.yhList[int(self.acorr.get_xlim()[1])-1] = int(yh)


		self.line1.set_xdata(np.arange(0,len(self.yList)))
		self.line1.set_ydata((self.yList))
		self.line2.set_xdata(np.arange(0,len(self.ybList)))
		self.line2.set_ydata((self.ybList))
		self.line8.set_xdata(np.arange(0,len(self.yhList)))
		self.line8.set_ydata((self.yhList))


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


		self.canvascorr.draw()
		self.canvastensao.draw()
		self.canvastemperatura.draw()
		

	
	def updateConv(self,dados,falhas=0):


		#Lê os valores do dicionário que contém os dados
		vcc1a = dados['values']['IE_101']
		vcc1b = dados['values']['IE_102']
		vcc1c = dados['values']['IE_103']
		vtc1a = dados['values']['EE_101']
		vtc1b = dados['values']['EE_102']
		vtc1c = dados['values']['EE_103']
		vcc3a = dados['values']['IE_301']
		vcc3b = dados['values']['IE_302']
		vcc3c = dados['values']['IE_303']
		vtc3a = dados['values']['EE_301']
		vtc3b = dados['values']['EE_302']
		vtc3c = dados['values']['EE_303']
		vtc2 = dados['values']['EE_201']
		vtb = dados['values']['EE_202']
		vtempc1 = dados['values']['TE_101']
		vtempc2 = dados['values']['TE_201']
		vtempc3 = dados['values']['TE_301']
		vtempbat = dados['values']['TE_202']
		vcbat = dados['values']['IE_201']
		vfreqc1 = dados['values']['SE_101']
		vrot = dados['values']['ST_301']


		#Destrói os Label antigos dos valores
		self.cc1a.destroy()
		self.cc1b.destroy()
		self.cc1c.destroy()
		self.tc1a.destroy()
		self.tc1b.destroy()
		self.tc1c.destroy()
		self.cc3a.destroy()
		self.cc3b.destroy()
		self.cc3c.destroy()
		self.tc3a.destroy()
		self.tc3b.destroy()
		self.tc3c.destroy()
		self.tc2.destroy()
		self.tb.destroy()
		self.tempc1.destroy()
		self.tempc2.destroy()
		self.tempc3.destroy()
		self.tempbat.destroy()
		self.cbat.destroy()
		self.freqc1.destroy()
		self.rot.destroy()
		

		#Cria os novos labels com os novos valores
		if 'EE_101' not in falhas:
			self.tc1a = Label(self,text=vtc1a,font=("Arial", 12))
			self.tc1a.place(x=458,y=30)
		else:
			self.tc1a = Label(self,text=vtc1a,font=("Arial", 12),foreground='#f00')
			self.tc1a.place(x=458,y=30)
		if 'EE_102' not in falhas:
			self.tc1b = Label(self,text=vtc1b,font=("Arial", 12))
			self.tc1b.place(x=458,y=85)
		else:
			self.tc1b = Label(self,text=vtc1b,font=("Arial", 12),foreground='#f00')
			self.tc1b.place(x=458,y=85)
		if 'EE_103' not in falhas:
			self.tc1c = Label(self,text=vtc1c,font=("Arial", 12))
			self.tc1c.place(x=458,y=140)
		else:
			self.tc1c = Label(self,text=vtc1c,font=("Arial", 12),foreground='#f00')
			self.tc1c.place(x=458,y=140)
		if 'IE_101' not in falhas:
			self.cc1a = Label(self,text=vcc1a,font=("Arial", 12))
			self.cc1a.place(x=520,y=30)
		else:
			self.cc1a = Label(self,text=vcc1a,font=("Arial", 12),foreground='#f00')
			self.cc1a.place(x=520,y=30)
		if 'IE_102' not in falhas:	
			self.cc1b = Label(self,text=vcc1b,font=("Arial", 12))
			self.cc1b.place(x=520,y=85)
		else:
			self.cc1b = Label(self,text=vcc1b,font=("Arial", 12),foreground='#f00')
			self.cc1b.place(x=520,y=85)
		if 'IE_103' not in falhas:	
			self.cc1c = Label(self,text=vcc1c,font=("Arial", 12))
			self.cc1c.place(x=520,y=140)
		else:
			self.cc1c = Label(self,text=vcc1c,font=("Arial", 12),foreground='#f00')
			self.cc1c.place(x=520,y=140)
		if 'EE_301' not in falhas:	
			self.tc3a = Label(self,text=vtc3a,font=("Arial", 12))
			self.tc3a.place(x=1141,y=30)
		else:
			self.tc3a = Label(self,text=vtc3a,font=("Arial", 12),foreground='#f00')
			self.tc3a.place(x=1141,y=30)
		if 'EE_302' not in falhas:	
			self.tc3b = Label(self,text=vtc3b,font=("Arial", 12))
			self.tc3b.place(x=1141,y=85)
		else:
			self.tc3b = Label(self,text=vtc3b,font=("Arial", 12),foreground='#f00')
			self.tc3b.place(x=1141,y=85)
		if 'EE_101' not in falhas:	
			self.tc3c = Label(self,text=vtc3c,font=("Arial", 12))
			self.tc3c.place(x=1141,y=140)
		else:
			self.tc3c = Label(self,text=vtc3c,font=("Arial", 12),foreground='#f00')
			self.tc3c.place(x=1141,y=140)
		if 'IE_301' not in falhas:	
			self.cc3a = Label(self,text=vcc3a,font=("Arial", 12))
			self.cc3a.place(x=1200,y=30)
		else:
			self.cc3a = Label(self,text=vcc3a,font=("Arial", 12),foreground='#f00')
			self.cc3a.place(x=1200,y=30)
		if 'IE_302' not in falhas:	
			self.cc3b = Label(self,text=vcc3b,font=("Arial", 12))
			self.cc3b.place(x=1200,y=85)
		else:
			self.cc3b = Label(self,text=vcc3b,font=("Arial", 12),foreground='#f00')
			self.cc3b.place(x=1200,y=85)
		if 'IE_303' not in falhas:	
			self.cc3c = Label(self,text=vcc3c,font=("Arial", 12))
			self.cc3c.place(x=1200,y=140)
		else:
			self.cc3c = Label(self,text=vcc3c,font=("Arial", 12),foreground='#f00')
			self.cc3c.place(x=1200,y=140)
		if 'EE_201' not in falhas:	
			self.tc2 = Label(self,text=vtc2,font=("Arial", 12))
			self.tc2.place(x=825,y=70)
		else:
			self.tc2 = Label(self,text=vtc2,font=("Arial", 12),foreground='#f00')
			self.tc2.place(x=825,y=70)
		if 'EE_202' not in falhas:	
			self.tb = Label(self,text=vtb,font=("Arial", 14))
			self.tb.place(x=990,y=340)
		else:
			self.tb = Label(self,text=vtb,font=("Arial", 14),foreground='#f00')
			self.tb.place(x=990,y=340)
		if 'TE_101' not in falhas:	
			self.tempc1 = Label(self,text=vtempc1,font=("Arial", 14))
			self.tempc1.place(x=645,y=165)
		else:
			self.tempc1 = Label(self,text=vtempc1,font=("Arial", 14),foreground='#f00')
			self.tempc1.place(x=645,y=165)
		if 'TE_201' not in falhas:	
			self.tempc2 = Label(self,text=vtempc2,font=("Arial", 14))
			self.tempc2.place(x=792,y=173)
		else:
			self.tempc2 = Label(self,text=vtempc2,font=("Arial", 14),foreground='#f00')
			self.tempc2.place(x=792,y=173)
		if 'TE_301' not in falhas:	
			self.tempc3 = Label(self,text=vtempc3,font=("Arial", 14))
			self.tempc3.place(x=1035,y=165)
		else:
			self.tempc3 = Label(self,text=vtempc3,font=("Arial", 14),foreground='#f00')
			self.tempc3.place(x=1035,y=165)
		if 'TE_202' not in falhas:	
			self.tempbat = Label(self,text=vtempbat,font=("Arial", 14))
			self.tempbat.place(x=998,y=300)
		else:
			self.tempbat = Label(self,text=vtempbat,font=("Arial", 14),foreground='#f00')
			self.tempbat.place(x=998,y=300)
		if 'IE_201' not in falhas:	
			self.cbat = Label(self,text=vcbat,font=("Arial", 14))
			self.cbat.place(x=955,y=400)
		else:
			self.cbat = Label(self,text=vcbat,font=("Arial", 14),foreground='#f00')
			self.cbat.place(x=955,y=400)
		if 'SE_101' not in falhas:	
			self.freqc1 = Label(self,text=vfreqc1,font=("Arial", 14))
			self.freqc1.place(x=575,y=165)
		else:
			self.freqc1 = Label(self,text=vfreqc1,font=("Arial", 14),foreground='#f00')
			self.freqc1.place(x=575,y=165)
		if 'ST_301' not in falhas:	
			self.rot = Label(self,text=vrot,font=("Arial", 13))
			self.rot.place(x=1275,y=150)
		else:
			self.rot = Label(self,text=vrot,font=("Arial", 13),foreground='#f00')
			self.rot.place(x=1275,y=150)
		try:
			self.falha.config(text = ",".join(falhas),fg='#f00')
		except:
			self.falha.config(text = '------')



	  