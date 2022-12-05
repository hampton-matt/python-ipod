import tkinter as tk
from PIL import ImageTk
from Resources.themes import Theme
from Resources.images import *

class Scrollbar(tk.Frame):
    # INIT
    def __init__(self, parent, theme: Theme, height, scale):  
        tk.Frame.__init__(self, parent)

        _padding = int(0*scale)
        _height = int(height-(_padding*2))
        _width = int(22*scale)
        _border = int(2*scale)

        self.scrollsize = 0.2
        self.postion = 0.005

        self.configure(bg=theme.bg)

        self.outer = tk.Frame(self, bg=theme.bg, highlightbackground=theme.fg, highlightthickness=_border, height=_height, width=_width)
        self.inner = tk.Frame(self.outer, bg=theme.fg, highlightthickness=0, width=_width, borderwidth=0)
        self.inner.place(in_=self.outer, relx=.5, rely=self.postion, anchor='n', relheight=self.scrollsize, relwidth=0.90)
        self.outer.pack()

    def set_size(self, total, pagesize):
        self.scrollsize = round(pagesize / total,1)
        self.inner.place(in_=self.outer, relx=.5, rely=self.postion, anchor='n', relheight=self.scrollsize, relwidth=0.90)


    def set_position(self, total, index):
        percentage = (index) / (total-1)
        position = round(percentage * self.scrollsize, 2)
        print(position)
        boundaries = max(.005, min(self.scrollsize-.005, position))
        self.postion = boundaries
        self.inner.place(in_=self.outer, relx=.5, rely=self.postion, anchor='n', relheight=self.scrollsize, relwidth=0.90)