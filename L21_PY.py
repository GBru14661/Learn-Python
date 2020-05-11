from tkinter import*
from tkinter import ttk
mainframe=Tk()

def calculate():
    result=0
    endResult.delete(0,END)

    num1=entNum1.get()
    num2=entNum2.get()

    if str(v.get())=='1':
        result=int(num1)+int(num2)
        entResult.insert("",str(result))
    elif str(v.get())=='2':
        result=int(num1)-int(num2)
        entResult.insert("",str(result))
    elif str(v.get())=='3':
        result=int(num1)*int(num2)
        entResult.insert9("",str(result))
    elif str(x.get())=='4':
        result=int(num1)/int(num2)
        entResult.insert("",str(result))

def clearEntry():
    entNum1.delete(0,END)
    entNum2.delete(0,END)
    entResult.delete(0,END)

lblframe1=ttk.LabelFrame(mainframe,text='โปรแกรมคำนวณ',labelanchor='n')
lblframe1.pack(padx=10,pady=10,side='left')

lblNum1=ttk.Label(lblframe1,text='ป้อนตัวเลขที่ 1:').grid(column=0,row=0,padx=5,sticky='e')
lblNum2=ttk.Label(lblframe1,text='ป้อนตัวเลขที่ 2:').grid(column=0,row=1,padx=5,sticky='e')
lblResult=ttk.Label(lblframe1,text='ผลลัพธ์:').grid(column=0,row=2,padx=5,sticky='e')

entNum1=ttk.Entry(lblframe1)
entNum2=ttk.Entry(lblframe1)
entResult=ttk.Entry(lblframe1)

entNum1.grid(column=1,row=0,padx=5)
entNum2.grid(column=1,row=1,padx=5)
entResult.grid(column=1,row=2,padx=5)

buttonEnter=ttk.Button(lblframe1,text='คำนวณ',command=calculate).grid(column=0,row=3,padx=5,pady=5)
buttonClear=ttk.Button(lblframe1,text='เคลัยร์',command=clearEntry).grid(column=1,row=3,padx=5,pady=5)

lblframe2=ttk.LabelFrame(mainframe,text='เลือกการคำนวณ',labelanchor='n')
lblframe2.pack(padx=10,pady=10)

v=StringVar(lblframe2,'1')
operations={'การบวก' : '1',
           'การลบ' : '2',
            'การคูณ' : "3",
            'การหาร' : '4'}
for (text,operations) in values.items():
    Radiobutton(lblframe2,text=text,vaiable=v,value=operation).pack(side=TOP,ipadx=4)

mainframe.mainloop()
