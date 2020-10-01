from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0,END)  

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file =None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        # textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),
        ("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def quitFile():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","This notepad is made using tkinter if any problem see tkinter documentation")


if __name__ == "__main__":
    root = Tk()
    root.geometry("644x688")
    root.title("TextEditor")
    root.wm_iconbitmap("icon.png")


    # Text area
    textArea = Text(root,font="Helvatica 15 bold")
    file = None
    textArea.pack(expand=True,fill=BOTH)
    # creating a menu bar
    menubar = Menu(root)

    # file menu  begins
    fileMenu = Menu(menubar,tearoff=0)

    fileMenu.add_command(label="New",command=newFile)

    fileMenu.add_command(label="Open",command=openFile)

    fileMenu.add_command(label="Save",command=saveFile)

    fileMenu.add_separator()

    fileMenu.add_command(label="Exit",command=quitFile)

    menubar.add_cascade(label="File",menu=fileMenu)
     # file menu ends

    # edit menu begins
    editMenu = Menu(menubar,tearoff=0)
    editMenu.add_command(label="Cut",command=cut)

    editMenu.add_command(label="Copy",command=copy)

    editMenu.add_command(label="Paste",command=paste)

    menubar.add_cascade(label="Edit",menu=editMenu)
    # edit menu ends
    
    # help menu starts
    helpMenu = Menu(menubar,tearoff=0)

    helpMenu.add_command(label="About Notepad",command = about)

    menubar.add_cascade(label="Help", menu=helpMenu)
    # help menu ends
    
    root.config(menu=menubar)
    
    # adding scroll bar
    scroll = Scrollbar(textArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)
    root.mainloop()
