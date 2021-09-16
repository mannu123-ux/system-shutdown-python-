from tkinter import*
import os
def shutdown():
    return os.system("shutdown/s /t 1")

def restart():
    return os.system("restart/r /t 1")

def logout():
    return os.system("logout -1")

window=Tk()
window.geometry('500x500')

Button(window,text="Shutdown",command=shutdown).grid(row=0)
Button(window,text="Restart",command=restart).grid(row=1)
Button(window,text="LogOut",command=logout).grid(row=2)

window.mainloop()
