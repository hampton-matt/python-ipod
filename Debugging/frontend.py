def hide_scroll(app):
    app.page.show_scroll(False)

def show_scroll(app):
    app.page.show_scroll(True)

def scalehalf(app):
    app.resize_manual(int(app.width*.5), int(app.height*.5))

def scaledouble(app):
    app.resize_manual(int(app.width*2), int(app.height*2))

def scalereset(app):
    app.resize_manual(320, 240)


commands = {
    "scroll 1" : show_scroll,
    "scroll 0" : hide_scroll,
    "scale .5" : scalehalf,
    "scale 2" : scaledouble,
    "scale -1" : scalereset,
}

descriptions = {
    "scroll" : "shows and hides scrollbar (scroll 0..1)",
    "scale" :  "scales the screen by .5, 2, -1 (reset)"
}