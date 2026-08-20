import tkinter as tk
from tkinter import messagebox

class DPIStackInspector():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty (self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def to_list (self):
        return list(self.items)



        