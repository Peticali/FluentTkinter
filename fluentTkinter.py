
from tkinter import *
import ctypes
from TkinterNEW import new

root = Tk()
root.config(bg='green')

root.wm_attributes("-transparent", 'green')
root.geometry('500x400')
root.update()

HWND = ctypes.windll.user32.GetForegroundWindow()

new.BlurWorkAround(root,HWND)
new.NewPanel()

l = new.NewLabel(text='New Widgets')
l.place(relx=.4,y=1)

#NewEntry
e = new.NewEntry(width=9)
e[1].insert(0,'Entry')
e[0].place(relx=.4,y=50)


#NewButton
b = new.NewButton(text='Button')
b[0].place(relx=.4,y=100)


#NewDropDown
choosed = StringVar() 
choosed.set('1')
objs = ['1','2','3'] #list 
b = new.NewDropDown(objs=objs,variable=choosed)
b[0].place(relx=.4,y=150)


root.mainloop()