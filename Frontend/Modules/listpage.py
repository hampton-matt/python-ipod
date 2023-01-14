import tkinter as tk
from Frontend.Resources.themes import Theme
from Frontend.Resources.images import *
from Frontend.Modules.listitem import ListItem
from Frontend.Modules.scrollbar import Scrollbar

class Listpage(tk.Frame):
    def __init__(self, parent, theme: Theme, pagesize, height, width, scale):  
        tk.Frame.__init__(self, parent)

        self.configure(bg=theme.bg)
        self.grid_columnconfigure(0, weight=1)
        self.index = 0
        self.offset = 0
        self.pagesize = pagesize
        self.scale = scale

        _row_height=int(height/pagesize)

        self.rows = {}
        for i in range(pagesize):
            self.rows[i] = ListItem(self, theme, scale, _row_height)
            self.rows[i].grid(row=i, column=0, sticky="nwe")
        self.set_selected(self.index)

        # Scrollbar
        self.scrollbar = Scrollbar(self, theme, height, scale)
        self.show_scroll(True)
        

    def set_selected(self, index):
        for row in self.rows:
            self.rows[row].selected(False)
        
        self.rows[index].selected(True)

    def show_scroll(self, show: bool):
        if show:
            self.scrollbar.grid(column=1, row=0, rowspan=self.pagesize, sticky="nse", padx=(2*self.scale, 0))
        else:
            self.scrollbar.grid_forget()

    def set_content(self, content, offset):
        if len(content) < self.pagesize:
            return
        for i in range(self.pagesize):
            self.rows[i].set_text(content[i])
        self.offset = offset