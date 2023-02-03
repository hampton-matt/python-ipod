# Themes Module
# Contians the theme object & access methods
if __name__ == "__main__":
    print("🔴 Package import only module")
    exit()

class Theme:
    def __init__(self, name, bg, fg, font, h1, h2, p):
        self.name = name
        self.bg = bg
        self.fg = fg
        self.font = font
        self.h1 = h1
        self.h2 = h2
        self.p = p


themes = {}
themes["default"] = (Theme("default", "#000000", "#1DB954", 'Helvetica', 16, 18, 14))
themes["light"] = (Theme("light", "#FFFFFF", "#111111", "Helvetica", 16, 18, 14))

def get_themes():
    return themes

def get_theme(theme):
    if theme in themes:
        return themes[theme]
    return themes["default"]