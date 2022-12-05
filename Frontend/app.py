import tkinter as tk
import Resources.themes as themes
import Modules.menubar as menu
from Modules.listitem import ListItem

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
        self.init_ui(scale)

    def init_ui(self, scale=None, pagesize=5):

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
        _row_height=int(self.content.winfo_height()/pagesize)

        rows = []
        for i in range(pagesize):
            rows.append(ListItem(self.content, self.theme, self.scale, _row_height))
            rows[i].grid(row=i, column=0,sticky="nwe")
            if i == 1:
                rows[i].selected(True)
            rows[i].update()
            print(rows[i].winfo_height())
            
            
        
        

        
    
    # Setters
    def refresh(self):
        if (self.queue_refresh > 0):
            self.container.destroy()
            self.init_ui(None, pagesize=5)
            self.queue_refresh -= 1


    def set_theme(self, theme):
        self.theme = themes.get_theme(theme)
        
    def resize(self, event):
        if(hasattr(event.widget, "is_root") and event.widget.is_root and (self.width != event.width or self.height != event.height)):
            self.width = event.width
            self.height = event.height
            self.queue_refresh = 2

# Debugging
if __name__ == "__main__":
    
    app = App(320, 240, "f")
    def loop():
        app.refresh()
        app.after(1000, loop)

    app.bind("<Configure>", app.resize)
    app.after(1000, loop)
    app.mainloop()