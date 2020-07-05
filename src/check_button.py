import tkinter as tk
from tkinter import ttk


class classCheckButton:
    def __init__(self, frame, filter, checkButtonName, callback):
        self.var = tk.IntVar(value=1)
        self.checkButtonName = checkButtonName
        self.filter = filter
        self._callback = callback
        checkbutton = tk.Checkbutton(
            frame, text=self.checkButtonName,
            variable=self.var,
            command=self.eventCheckButton)
        checkbutton.pack(anchor="w")

    def get(self):
        return self.var.get()

    def eventCheckButton(self):
        print("%s: checkButton=%d" % (self.checkButtonName, self.var.get()))
        if self._callback:
            self._callback()