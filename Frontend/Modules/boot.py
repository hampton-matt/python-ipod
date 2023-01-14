# Boot
# FILE - boot.py
# DESC - Boot object that contains the Tkinter structure for the boot module
if __name__ == "__main__":
    print("🔴 Root import only module")
    exit()

from tkinter import tk
from Frontend.Resources.themes import Theme
from Frontend.Resources.images import *


class Boot(tk.Frame):
    def __init__(self, parent, theme: Theme, scale, height, width):
        super().__init__(self, parent)

        self.configure(bg=theme.bg, height=height, width=width)

        
