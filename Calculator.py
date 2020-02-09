from tkinter import Tk,Button,Label,Frame,BOTH,X,SE,RIDGE,GROOVE,LEFT
from tkinter.messagebox import showwarning

class Calculator:
    
    def __init__(self,root):
        self.root = root
        self.buttons = []
        self.row = []
        self.ans = None
        self.draw()
        
    def draw(self):
        self.ans = Label(self.root, text="0", font="Arial 20", anchor=SE, relief=RIDGE, bg="White", height=2)
        self.ans.pack(expand=True, fill=BOTH)
        
        clear = Button(self.root,text="Clear", font="Arial 11", relief=GROOVE, bd=0)
        clear.pack(fill=X)
        clear.bind("<Enter>", self.onHover)
        clear.bind("<Leave>", self.onHoverOut)
        clear.bind("<Button-1>", self.onClick)
        
        for i in range(4):
            r = Frame(self.root)
            r.pack(expand=True, fill=BOTH)
            self.row.append(r)
        
        for i in range(4):
            for j in range(4):
                btn = Button(self.row[i],text=j, relief=GROOVE, bd=0, font="Arial 20")
                btn.pack(side=LEFT, expand=True, fill=BOTH)
                self.buttons.append(btn)
                del btn
                
        for i in self.buttons:
            i.bind("<Enter>", self.onHover)
            i.bind("<Leave>", self.onHoverOut)
            i.bind("<Button-1>", self.onClick)
        
        self.buttons[0].config(text="7")
        self.buttons[1].config(text="8")
        self.buttons[2].config(text="9")
        self.buttons[3].config(text="/")
        self.buttons[4].config(text="4")
        self.buttons[5].config(text="5")
        self.buttons[6].config(text="6")
        self.buttons[7].config(text="*")
        self.buttons[8].config(text="1")
        self.buttons[9].config(text="2")
        self.buttons[10].config(text="3")
        self.buttons[11].config(text="-")
        self.buttons[12].config(text=".")
        self.buttons[13].config(text="0")
        self.buttons[14].config(text="=")
        self.buttons[15].config(text="+")
                
    def onHover(self, event):
        event.widget.config(bg="#bdc3c7")
    
    def onHoverOut(self, event):
        event.widget.config(bg=self.root["bg"])
        
    def onClick(self, event):  
        ans = self.ans["text"]
        if event.widget["text"] == "=":
            self.equate(ans)
            return
        if event.widget["text"] == "Clear":
            self.clear()
            return
        l = ["/","*","-","+","."]
        l2 = ["/","*"]
        if ans[-1] in l and event.widget["text"] in l:
            ans = ans[0:len(ans)-1] + event.widget["text"]
            self.ans.config(text=ans)
            return
        ans = event.widget["text"] if ans ==  "0" or ans in l2 else ans + event.widget["text"]
        self.ans.config(text=ans)   
        
    def equate(self, exp):
        try:
            self.ans.config(text=eval(exp))
        except ZeroDivisionError as e:
            showwarning("Warning", e)
            self.clear()
    
    def clear(self):
        self.ans.config(text="0")
        
master = Tk()
master.title("Calculator")
master.geometry("250x400+800+200")
master.resizable(False, False)
calculator = Calculator(master)
master.mainloop()
