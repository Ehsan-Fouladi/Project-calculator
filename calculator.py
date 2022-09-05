from tkinter import *



def fCalc(src, side):
    appObj = Frame(src, borderwidth=4, bd=2, bg ="blue")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj 
 
def button(src, side, text, command=None):
    appObj = Button(src, text=text, command=command, bg="HotPink")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj
 
class app(Frame):
    def __init__(self, root = Tk(), width=364, height=425):
        Frame.__init__(self)
        self.option_add("*Font", 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/3) - (width/3)
        y = (screen_height/3) - (height/3)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        display = StringVar()
        Entry(self, relief= RIDGE,      
                    textvariable=display, state=DISABLED, justify='left', bd=20, bg="white").pack(side=TOP, expand=YES,
                            fill=BOTH)
        
        clrChar = "Delete"
        Edit = "Edit"
        button(self, TOP, clrChar,lambda appObj=display, i=clrChar: appObj.set(''))
        button(self, TOP, Edit,lambda appObj=display, b=Edit: appObj.set(''))
 
 
        for btnNum in ("789/", "456*", "0123-", "π.+√",
                                "()","{}","[]","<>"):
 
            FunctionNum = fCalc(self, TOP)
            for fEquals in btnNum:
                button(FunctionNum, LEFT, fEquals,
                        lambda appObj=display, i=fEquals: appObj.set(appObj.get() + i))
                EqualsButton = fCalc(self, TOP)
                
        for fEquals in "=":
            if fEquals == "=":
                btnEquals = button(EqualsButton, LEFT, fEquals)
                btnEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, appObj=display: s.result(appObj), "+")
            else:
                btnEquals = button(EqualsButton, LEFT, fEquals,
                        lambda appObj=display, s=" %s "%fEquals: appObj.set(appObj.get()+s))
 
    def result(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR CODE")

if __name__ == '__main__':
    app().mainloop()