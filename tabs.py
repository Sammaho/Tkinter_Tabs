'''
Created by Sam Wandler to be used an extension to Tkinter
This class creates tabs/frames that can be toggled by buttons at the top of the screens
'''

from tkinter import *


class Tab:
    def __init__(self, frame, text='tab1', relief='groove'):
        # Creates the main frame which has all widgets in it
        self.main_frame = Frame(frame, bd=2, relief=relief)
        self.location=0
        # Creates the top frame, which is used to select the different widgets.
        self.button_frame = Frame(self.main_frame)
        self.frames = []
        self.buttons = []
        # self.insert_top()
        self.insert_tab(text=text)

    # This is when a tab is clicked, the tab becomes active/visible and the active tab does not
    def __tab_clicked(self, text, location_index):
        # Disables and raises button that is clicked
        self.buttons[location_index.get()].config(relief='flat', state='disabled', cursor='arrow')
        # Enables and sinks button that used to be clicked
        self.buttons[self.location].config(relief='sunken', state='normal', cursor='hand2')

        self.frames[self.location].grid_forget()
        self.frames[location_index.get()].grid(row=1, column=0)

        # updates tab that is opened
        self.location = location_index.get()
        print('clicked')

    def create_button(self, location_index=0, location=0, text='tab'):
        print('self location=', self.location, 'location =', location)
        # keeps the location recessed, but all others not
        if location == self.location:
            # Keeps first tab height of everyting else
            tab_button = Button(self.button_frame, text=text, relief='flat',
                                command=lambda:self.__tab_clicked(text, location_index),
                                state='disabled', disabledforeground='black')
        else:
            # Sinks all tabs, but the active one.
            tab_button = Button(self.button_frame, text=text, cursor='hand2', relief="sunken",
                                command=lambda:self.__tab_clicked(text, location_index), disabledforeground='black')
        return tab_button

    # Inserts the top buttons
    def __insert_top(self, text='tab'):
        location_index = IntVar()
        tab_button = self.create_button(location=len(self.frames)-1, text=text, location_index=location_index)
        self.buttons.append(tab_button)

        # This is so it can keep track of its location
        location_index.set(len(self.frames)-1)
        tab_button.grid(row=0, column=len(self.frames)-1)

    def insert_tab(self, text='tab'):
        new_tab = Frame(self.main_frame)
        new_label = Label(new_tab, text='my label ' + str(len(self.frames) + 1))
        new_label.pack()
        self.frames.append(new_tab)
        self.__insert_top(text=text)

    def __place_widgets(self):
        self.button_frame.grid(row=0, column=0)
        self.frames[self.location].grid(row=1, column=0)

    def pack(self):
        self.__place_widgets()
        self.main_frame.pack()

    def grid(self, row=0, column=0):
        self.__place_widgets()
        self.main_frame.grid(row=row, column=column)

    # This allows you to return the tabs as frames so that you can populate the tabs from the other program.
    def tab(self, index):
        return self.frames[index]

