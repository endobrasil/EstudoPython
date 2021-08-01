#manipulando janelas com python
import webbrowser
from tkinter import *

root = Tk( )
root.title('Abrir o browser')
root.gometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle=Button(root, text='Abrir o google', command=google).pack(pady=20)
root.mainloop()