from tkinter import *




def calc(root, side):
    screen = Frame(root, borderwidth=3, bd=3, bg='light blue')
    screen.pack(side=TOP, expand=YES, fill=BOTH)
    return screen


def button(root, side, text, command=NONE):
    screen = Button(root, text=text, command=command)
    screen.pack(side=LEFT, expand=YES, fill=BOTH)
    return screen


class calCu(Frame):
        def __init__(self, master):
            Frame.__init__(self)
            self.pack(expand=YES, fill=BOTH)
            self.master.title('CALCULATOR')

            txt = StringVar()
            Entry(self, relief=RIDGE, textvariable=txt, justify='right', bd=3, bg='light blue').pack(side=TOP, expand=YES,fill=BOTH)
            for cbutton in (["CE"], ["C"]):
                erase = calc(self, TOP)
                for i in cbutton:
                    button(erase,LEFT, text=i, command=lambda screen=txt, q=i: screen.set(""))

            for num in ("123/", "456*", "789+", "0.-"):
                func=calc(self,TOP)
                for i in num:
                    button(func, LEFT, i, command=lambda screen=txt, q=i: screen.set(screen.get()+q))


            ebutton=calc(self,TOP)
            for i in "=":
                if i =="=":
                    bequal = button(ebutton, LEFT, i)
                    bequal.bind('<ButtonRelease-1>',
                                lambda e,s=self,screen=txt:s.ca(screen),'+')
                else:
                    bequal = button(ebutton, LEFT, i, command=lambda screen=txt, s='%s'%i: screen.set(screen.get()+s))

        def ca(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.get("'ERROR")

root = Tk()
a = calCu(root)
root.mainloop()
