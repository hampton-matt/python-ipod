if __name__ == "__main__":
    print("🔴 Root import only module")
    exit()

import tkinter as tk
from PIL import ImageTk
from Frontend.Resources.themes import Theme
from Frontend.Resources.images import *

class NowPlaying(tk.Frame):
    def __init__(self, parent, theme: Theme, pagesize, height, width, scale):  
        tk.Frame.__init__(self, parent)

        self.configure(bg=theme.bg)
        self.grid_columnconfigure(0, weight=1)
        h1 = (theme.font, int(theme.h2*scale))
        p = (theme.font, int(theme.p*scale))
        _padding = int(scale*4)
        _width = int(width - (_padding*2))
        self.position = tk.Label(self, text="15 of 32", bg=theme.bg, fg=theme.fg, font=p, anchor='w')
        self.position.grid(row=0, column=0, sticky='nwe', pady=(int(scale*5),0))  

        self.song = tk.Label(self, text="Alone Again, Naturally", bg=theme.bg, fg=theme.fg, font=h1, anchor='center')
        self.song.grid(row=1, column=0, sticky='nwe', pady=(int(scale*15), 0))

        self.artist = tk.Label(self, text="Red Hot Chilli Peppers", bg=theme.bg, fg=theme.fg, font=h1, anchor='center')
        self.artist.grid(row=2, column=0, sticky='nwe', pady=(int(scale*3), int(scale*3)))

        self.album = tk.Label(self, text="Vulfmon", bg=theme.bg, fg=theme.fg, font=h1, anchor='center')
        self.album.grid(row=3, column=0, sticky='nwe', pady=(0, int(scale*12)))

        self.progressframeimg = ImageTk.PhotoImage(resize(get_image(IMG_TIMELINE, fg = theme.fg, bg = theme.bg), width=_width))
        self.progressbarimg = ImageTk.PhotoImage(resize(get_image(IMG_TIMELINE_FILL, fg = theme.fg, bg = theme.bg), width=_width))
        self.progress = tk.Canvas(self, bg=theme.fg, highlightthickness=0, borderwidth=0, height=self.progressbarimg.height())
        self.progressframe= tk.Label(self.progress, image=self.progressframeimg, borderwidth=0, bg=theme.bg, anchor='w')
        self.progressframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.progressbar = tk.Label(self.progress, image=self.progressbarimg, borderwidth=0, bg=theme.bg, anchor='w')
        self.progressbar.place(relx=0, rely=0, x=0, relwidth=1, relheight=1)
        self.progress.grid(row=4, column=0, sticky='nwe', pady=(int(scale*5), 0), padx=_padding)

        timelinegrid = tk.Canvas(self, bg=theme.bg, borderwidth=0, highlightthickness=0)
        timelinegrid.grid(row=5, column=0, sticky="new", padx=_padding, pady=((int(scale*4))))
        timelinegrid.grid_propagate(0)
        timelinegrid.grid_columnconfigure(0, weight=1)
        timelinegrid.grid_columnconfigure(1, weight=1)

        self.currenttime = tk.Label(timelinegrid, text="0:40", bg=theme.bg, fg=theme.fg, font=p, anchor='w', justify='left')
        self.currenttime.grid(row=0, column=0, sticky='nw')
        self.remainingtime = tk.Label(timelinegrid, text="-2:16", bg=theme.bg, fg=theme.fg, font=p, anchor='e')
        self.remainingtime.grid(row=0, column=1, sticky='ne')