import tkinter as tk
from PIL import ImageTk
from Frontend.Resources.themes import Theme
from Frontend.Resources.images import *

class MenuBar(tk.Frame):
    # INIT
    def __init__(self, parent, theme: Theme, scale, title="sPod"):  
        tk.Frame.__init__(self, parent)

        _height = int(20 * scale)

        # Images
        self.play_image = ImageTk.PhotoImage(resize(get_image(IMG_PLAY, fg = theme.fg, bg = theme.bg), height=_height))
        self.pause_image = ImageTk.PhotoImage(resize(get_image(IMG_PAUSE, fg = theme.fg, bg = theme.bg), height=_height))
        self.nowifi_image = ImageTk.PhotoImage(resize(get_image(IMG_NO_WIFI, fg = theme.fg, bg = theme.bg), height=_height))
        self.wifi_image = ImageTk.PhotoImage(resize(get_image(IMG_WIFI, fg = theme.fg, bg = theme.bg), height=_height))
        self.blank_image = ImageTk.PhotoImage(resize(get_image(IMG_BLANK, fg = theme.fg, bg = theme.bg), height=_height))

        # UI
        self.configure(bg=theme.bg)
        self.grid_columnconfigure(1, weight=1)

        self.left = tk.Label(self, image=self.blank_image, height=_height, width=_height, background=theme.bg, padx=2, pady=2)
        self.left.grid(sticky='w', column=0, row=0)

        self.header = tk.Label(self, text=title, font=(theme.font, int(theme.h1*scale)), background=theme.bg, foreground=theme.fg) 
        self.header.grid(sticky='we', column=1, row=0, padx=int(scale*10))

        self.right = tk.Label(self, image=self.nowifi_image, height=_height, width=_height, background=theme.bg)
        self.right.grid(sticky='e', column=2, row=0)

        self.divider = tk.Canvas(self, bg=theme.fg, highlightthickness=0, height=(2*scale), relief='flat')
        self.divider.grid(sticky='we', column=0, row=1, columnspan=3, pady=(2*scale))

    # SETTERS
    def set_header(self, title):
        self.header.configure(text=title)

    def set_wifi(self, connected: bool):
        if connected:
            self.right.configure(image=self.wifi_image)
        else:
            self.right.configure(image=self.nowifi_image)

    def set_status(self, playing: bool):
        if playing:
            self.left.configure(image=self.play_image)
        else:
            self.left.configure(image=self.pause_image)
