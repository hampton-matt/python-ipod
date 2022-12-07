if __name__ == "__main__":
    print("🔴 Root import only module")
    exit()

import tkinter as tk
import Frontend.Resources.themes as themes
import Frontend.Modules.menubar as menu
from Frontend.Modules.listpage import Listpage
from Frontend.Modules.nowplaying import NowPlaying
from Frontend.Modules.scrollbar import Scrollbar

class App(tk.Tk):
    # INIT
    # ARGS - Resolution - Theme Object
    def __init__(self, width, height, theme="default", scale=None, pagesize=5):
        tk.Tk.__init__(self)

        # Variable
        self.is_root = True
        self.width = width
        self.height = height
        self.theme = themes.get_theme(theme)
        self.geometry("%sx%s" % (self.width, self.height))
        self.configure(bg=self.theme.bg)
        self.queue_refresh = 0
        self.pagesize = pagesize
        self.init_ui(scale)

    def init_ui(self, scale=None):

        # Scale Check
        # Finds the minimum scale value for width and height versus 320 x 240
        if scale is None:
            self.scale = round(min((self.width / 320), (self.height / 240)),2)
        else:
            self.scale = scale

        # Container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True, padx=int(8*self.scale), pady=(5,10))
        self.container.configure(bg=self.theme.bg)
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(1, weight=1)

        # Menu
        self.menu = menu.MenuBar(self.container, self.theme, self.scale)
        self.menu.grid(row=0, column=0, sticky="nwe")

        # Content
        self.content = tk.Frame(self.container, background=self.theme.bg)
        self.content.grid(row=1, column=0, sticky="news")
        self.content.grid_columnconfigure(0, weight=1)

        # Calculate Content size and row height
        self.content.update()
        _height = self.content.winfo_height()
        _width = self.content.winfo_width()

        self.page = NowPlaying(self.content, self.theme, self.pagesize, _height, _width, self.scale)
        self.page.grid(row=0, column=0, sticky="nsew")
        
    
    # Setters
    def refresh(self):
        if (self.queue_refresh > 0):
            self.container.destroy()
            self.init_ui(None)
            self.queue_refresh -= 1


    def set_theme(self, theme):
        self.theme = themes.get_theme(theme)

    def resize_manual(self, width, height):
        self.width = width
        self.height = height
        self.geometry("%sx%s" % (self.width, self.height))
        self.queue_refresh = 2
        
    def resize(self, event):
        if(hasattr(event.widget, "is_root") and event.widget.is_root and (self.width != event.width or self.height != event.height)):
            self.width = event.width
            self.height = event.height
            self.queue_refresh = 2