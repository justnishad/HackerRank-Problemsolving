from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Time Converter')
window.geometry('400x200')
window.configure(bg='#009688')


def getData():
    x=txt.get()
    print(x)
    convert(x)
    #lbl2.configure(text=x)
def convert(s1):
    x=0
    hh='00'
    mm='00'
    ss='00'
    for i in range(0,len(s1)): 
     if(i==0 and i+1==1):
         hh=s1[i]+s1[i+1]
         i=2
     elif(i==3 and i+1==4):
         mm=s1[i]+s1[i+1]
         i=5
     elif(i==6 and i+1==7):
         ss=s1[i]+s1[i+1]
     elif(i==8):
         if(s1[i]=='P' or s1[i]=='p'):
             x=1

    if(x==1):
      if(hh=='12'):
        messagebox.showinfo("Result",hh+':'+mm+':'+ss)
      else:    
         hh1=int(hh)+12
         messagebox.showinfo("Result",str(hh1)+':'+mm+':'+ss)

    else:
      if(hh=='12'):
         hh2=int(hh)-12
         messagebox.showinfo("Result",str(hh2)+'0:'+mm+':'+ss)
      else:  
         messagebox.showinfo("Result",hh+':'+mm+':'+ss)



lbl=Label(window,text='Enter the time in 12 Hour Format\n\t',bg='#009688',fg='black',font=('Arial Bold',10))
lbl.grid(column=0, row=0)
txt = Entry(window,width=27)
txt.grid(column=0, row=2)

lbl1=Label(window,text='\t',bg='#009688')
lbl1.grid(column=1, row=2)
btn = Button(window, text="Convert",bg='#37474F',fg='white',command=getData)
btn.grid(column=1, row=2)
window.mainloop()
