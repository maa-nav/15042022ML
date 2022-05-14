import tkinter as tkr
from tkinter import ttk
from tkinter import messagebox
import tkinter.filedialog as tkfd
##from PIL import ImageTk,Image 


app = tkr.Tk(__name__)
app.geometry('500x800')
app.title('testApp')
##
##tkr.Label(app,text = 'Hello',font=('Arial',20),fg='red',bg='cyan').place(x=10,y=10)
##tkr.Label(app,text = 'world').place(x=100,y=100)
##tkr.Label(app,text = 'Ravi and Yudi').place(x=200,y=150)

##tkr.Label(app,text = 'Hello',font=('Arial',20),fg='red',bg='cyan').pack(anchor=tkr.NW)
##tkr.Label(app,text = 'world').pack(anchor=tkr.W)
##tkr.Label(app,text = 'Ravi and Yudi').pack(anchor=tkr.CENTER)
##
##tkr.Label(app,text = 'Hello',font=('Arial',20),fg='red',bg='cyan').grid(row = 2,column=1)
##tkr.Label(app,text = 'world').grid(row = 1,column=1)
##tkr.Label(app,text = 'Ravi and Yudi').grid(row = 0,column=0)



def show():
    print(ent.get())
    print(msg.get())
    msg.set(ent.get())
    print(cb1.get())
    print(rb1.get())
    print(sb1.get())
    if not curs():lab.set('Please select one value from listbox')
        #messagebox.showerror('Error','Please select one value from listbox')
    else: print(list_box.get(curs()),curs());lab.set('')

####### Entry #####

ent = tkr.Variable(app)
tkr.Entry(app,textvariable=ent,font=(30),width=11).pack()

###### button ######

tkr.Button(app,text='submit',command = show).pack()

##### Message ######

msg = tkr.Variable(app)
msg.set('HEllo world welcome to python')
tkr.Message(app,textvariable=msg).pack()

##### Checkbutton #######

cb1 = tkr.Variable(app,'1')
tkr.Checkbutton(app,text='python',variable=cb1,onvalue=1,offvalue=0).pack()

###### Radiobutton ######

rb1 = tkr.Variable(app,'0')
rb_values = {'ML':'1','AI':'2'}
for k,v in rb_values.items():
    tkr.Radiobutton(app,text=k,variable=rb1,value=v).pack()


###### Spin box ######

sb1 = tkr.Variable(app)
tkr.Spinbox(app,from_ = 1,to = 12,textvariable=sb1).pack()

####### option ######

opt  = tkr.Variable(app)
opt_values = ('python','java','C++')
ttk.OptionMenu(app,opt,*opt_values).pack()

###### Combobox #######
ck_values = ('hello','audi','BMW','benz')
cb = tkr.Variable(app)
Combo_box = ttk.Combobox(app,value = ck_values,textvariable=cb)
Combo_box.pack()

####### Listbox #####

#lb = tkr.Variabe
list_box = tkr.Listbox(app,height=5,activestyle='dotbox',fg='white',bg='black')
listvalues = ['Endgame','Doctor Strange','Kgf','Batman','Peaky Blinders','hello','world']
for i in listvalues:
    list_box.insert(tkr.END,i)
list_box.select_set(1)
curs = list_box.curselection
list_box.pack()


####### Warning Label #######

lab = tkr.Variable(app)
tkr.Label(app,textvariable=lab,text=lab.get(),fg='red',font=('Arial',7,'bold italic')).pack()


######### Inserting Image #############

##def selection():
##    global cnv
##    global img
##    file = tkfd.askopenfiles(mode='r',filetypes=[('Images','*.png')])
##    print(file)
##    if file:
##        Img_name = file[0].name
##        img1 = Image.open(Img_name)
##        img1 = img1.resize((200,200))
##        img = ImageTk.PhotoImage(img1)
##        cnv.create_image(125,125,anchor=tkr.CENTER,image = img)
##
##
##
##tkr.Button(app,text='browse Image',command = selection).pack()
##cnv = tkr.Canvas(app,width=250,height=250,bg='cyan')
##cnv.pack()


app.mainloop()
