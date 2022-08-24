from tkinter import *
from tabs import Tab

root = Tk()
tab = Tab(root, text='mytab')
tab.insert_tab(text='I love how well this is coming together')
tab.insert_tab(text='Third')
tab.insert_tab()
tab.insert_tab()
tab.grid(row=0, column=0)

tab2 = Tab(root, text='Slime Rancher')
tab2.insert_tab(text='Tabby 2')
tab2.insert_tab(text='What is up')

def text_clicked():
    print('text button was clicked')

test_button = Button(tab2.tab(1), text='test button', command=text_clicked)
test_button.pack()

tab2.grid(row=1, column=1)

root.mainloop()