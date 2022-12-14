import tkinter as tk
from pathlib import Path
from PIL import ImageTk
from Resources.themes import Theme
from Resources.images import *

class ListItem(tk.Frame):
    def __init__(self, parent, theme: Theme, scale, rowheight):  
        tk.Frame.__init__(self, parent)

        _height = int(scale*20)
        self.padding = int((rowheight - _height) / 2)

        print(rowheight, _height, self.padding)
        self.scale = scale
        self.theme = theme

        self.configure(bg=theme.bg)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.arrow_image = ImageTk.PhotoImage(resize(get_image(IMG_ARROW, fg = theme.bg), height=_height))
        
        self.left = tk.Label(self, padx=int(2*scale), text="Placeholder", fg=theme.fg, bg=theme.bg, anchor="w", font=(theme.font, int(theme.p * scale)), borderwidth=0)
        self.left.grid(row=0, column=0, sticky="ew")
        
        self.right = tk.Label(self, image=self.arrow_image, bg=theme.bg, height=_height, pady=0, borderwidth=0)
        self.right.grid(row=0, column=1, sticky="es", pady=self.padding, padx=int(4*self.scale))

        self.left.update()
        print(self.left.winfo_height())

    def selected(self, selected: bool):
        if selected:
            self.configure(bg=self.theme.fg)
            self.right.configure(bg=self.theme.fg)
            self.left.configure(bg=self.theme.fg, fg=self.theme.bg)
        else:
            self.configure(bg=self.theme.bg)
            self.right.configure(bg=self.theme.bg)
            self.left.configure(bg=self.theme.fg, fg=self.theme.bg)