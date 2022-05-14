import tkinter as tkr
app = tkr.Tk(__name__)
app.title('Calc')
app.geometry('350x450')

####### Label #######

tkr.Label(app,text='Calculator',font=('Times',25),fg='red').place(x=110,y=20)
tkr.Label(app,text='First Value',font=('Times',10),fg='black').place(x=30,y=60)
tkr.Label(app,text='Second Value',font=('Times',10),fg='black').place(x=200,y=60)

####### Entry #######

en1 = tkr.Variable(app)
tkr.Entry(app,textvariable=en1,font=('Times',15),fg='blue',width=10).place(x=30,y=80)
en2 = tkr.Variable(app)
tkr.Entry(app,textvariable=en2,font=('Times',15),fg='red',width=10).place(x=200,y=80)


####### Button ####


def process(optr):
    res.set('%.2f'%eval(en1.get()+ optr +en2.get()))

tkr.Button(app,text='+',bg = 'yellow',fg = 'red',font=('Arial',20),
           command=lambda:process('+')).place(x=50,y=130)
tkr.Button(app,text='-',bg = 'yellow',fg = 'red',font=('Arial',20),
           command=lambda:process('-')).place(x=100,y=130)
tkr.Button(app,text='*',bg = 'yellow',fg = 'red',font=('Arial',20),
           command=lambda:process('*')).place(x=150,y=130)
tkr.Button(app,text='/',bg = 'yellow',fg = 'red',font=('Arial',20),
           command=lambda:process('/')).place(x=200,y=130)


#### Result label #####
tkr.Label(app,text='Result:',font=('Comic Sans',25)).place(x=100,y=250)
res = tkr.Variable(app)
res.set('0')
tkr.Label(app,text=res.get(),font=('Comic Sans',25),
          textvariable=res,bg='grey',fg='green').place(x=100,y=300)


app.mainloop()

