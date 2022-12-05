import tkinter as tk
import Resources.themes as themes
import Modules.menubar as menu
from Modules.listitem import ListItem
from Modules.scrollbar import Scrollbar

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
        _row_height=int(_height/self.pagesize)

        # Scrollbar
        self.scrollbar = Scrollbar(self.content, self.theme, _height, self.scale)
        self.scrollbar.grid(column=1, row=0, rowspan=self.pagesize, sticky="nse")
        

        rows = []
        for i in range(self.pagesize):
            rows.append(ListItem(self.content, self.theme, self.scale, _row_height))
            rows[i].grid(row=i, column=0,sticky="nwe")
            if i == 1:
                rows[i].selected(True)
    
    # Setters
    def refresh(self):
        if (self.queue_refresh > 0):
            self.container.destroy()
            self.init_ui(None, pagesize=self.pagesize)
            self.queue_refresh -= 1


    def set_theme(self, theme):
        self.theme = themes.get_theme(theme)
        
    def resize(self, event):
        if(hasattr(event.widget, "is_root") and event.widget.is_root and (self.width != event.width or self.height != event.height)):
            self.width = event.width
            self.height = event.height
            self.queue_refresh = 2

    def show_scroll(self, show: bool):
        if show:
            self.scrollbar.grid(column=1, row=0, rowspan=self.pagesize, sticky="nse")
        else:
            self.scrollbar.grid_forget()


# Debugging
if __name__ == "__main__":
    
    app = App(320, 240, "dark")
    def loop():
        app.refresh()
        app.after(1000, loop)


    def test_scroll():
        app.refresh()
        total = int(input("Total: "))
        app.scrollbar.set_size(total, int(input("Pagesize: ")))
        app.scrollbar.set_position(total, int(input("Index: ")))
        app.after(1000, test_scroll)

    app.bind("<Configure>", app.resize)
    app.after(5000, loop)
    app.mainloop()