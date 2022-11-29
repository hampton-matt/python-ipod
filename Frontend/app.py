import tkinter as tk
import Resources.themes as themes

class App(tk.Tk):
    # INIT
    # ARGS - Resolution - Theme Object
    def __init__(self, width, height, scale, theme):
        tk.Tk.__init__(self)

        # Variable
        self.width = width
        self.height = height
        self.theme = themes.get_theme(theme)
        self.h1 = (self.theme.font, self.theme.h1)
        self.p = (self.theme.font, self.theme.p)
        self.geometry("%sx%s" % (self.width, self.height))
        self.configure(bg=self.theme.bg)

        # Scale Check
        # Finds the minimum scale value for width and height versus 320 x 240
        if scale is None:
            self.scale = round(min((self.width / 320), (self.height / 240)),2)
        else:
            self.scale = scale

        # Container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=10, pady=(5,10))
        container.configure(bg=self.theme.bg)
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(1, weight=1)

    
    # Setters
    def refresh(self):
        self.destroy()
        self.__init__(str(self.width), str(self.height), self.scale, self.theme.name)

    def set_theme(self, theme):
        self.theme = themes.get_theme(theme)
        


# Debugging
if __name__ == "__main__":
    app = App(320, 240, None, "default")
    def test():
        app.set_theme("light")
        app.refresh()
    app.after(5000, test)
    app.mainloop()