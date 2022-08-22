from tkinter import *
from tabs import Tab

root = Tk()
tab = Tab(root, text='mytab')
tab.insert_tab(text='Sam')
tab.insert_tab(text='Third')
tab.insert_tab()
tab.insert_tab()
tab.grid(row=0, column=0)

tab2 = Tab(root, text='Slime Rancher')
tab2.insert_tab(text='Tabby 2')
tab2.insert_tab(text='Jennie')
tab2.grid(row=1,column=1)

root.mainloop()