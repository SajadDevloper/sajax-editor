# Import
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import sys
 
 
appName = 'Sajax editor'
nofileOpenedString = 'New File'

currentFilePath = nofileOpenedString

fileTypes = [("Text Document","*.txt"), ("C# Source File","*.cs"), ("HTML Document","*.html"), ("Markdown","*.md"), ("css Document","*.css"), ("Java Source File","*.java")]

window = Tk()

window.grid_columnconfigure(0, weight=1)

window.title(appName + " - " + currentFilePath)

window.geometry('500x400')

def fileDropDownHandeler(action):
    global currentFilePath

    if action == "open":
        file = filedialog.askopenfilename(filetypes = fileTypes)

        window.title(appName + " - " + file)

        currentFilePath = file

        with open(file, 'r') as f:
            txt.delete(1.0,END)
            txt.insert(INSERT,f.read())

    elif action == "new":
        currentFilePath = nofileOpenedString
        txt.delete(1.0,END)
        window.title(appName + " - " + currentFilePath)

    elif action == "save" or action == "saveAs":
        if currentFilePath == nofileOpenedString or action=='saveAs':
            currentFilePath = filedialog.asksaveasfilename(filetypes = fileTypes)

        with open(currentFilePath, 'w') as f:
            f.write(txt.get('1.0','end'))

        window.title(appName + " - " + currentFilePath)

def textchange(event):
    window.title(appName + " - *" + currentFilePath)

txt = scrolledtext.ScrolledText(window, height=999)
txt.grid(row=1,sticky=N+S+E+W)

txt.bind('<KeyPress>', textchange)

menu = Menu(window)

fileDropdown = Menu(menu, tearoff=False)

fileDropdown.add_command(label='New', command=lambda: fileDropDownHandeler("new"))
fileDropdown.add_command(label='Open', command=lambda: fileDropDownHandeler("open"))

fileDropdown.add_separator()
fileDropdown.add_command(label='Save', command=lambda: fileDropDownHandeler("save"))
fileDropdown.add_command(label='Save as', command=lambda: fileDropDownHandeler("saveAs"))

menu.add_cascade(label='File', menu=fileDropdown)

window.config(menu=menu)

if len(sys.argv) == 2:
    currentFilePath = sys.argv[1]

    window.title(appName + " - " + currentFilePath)

    with open(currentFilePath, 'r') as f:
        txt.delete(1.0,END)
        txt.insert(INSERT,f.read())

window.mainloop()
