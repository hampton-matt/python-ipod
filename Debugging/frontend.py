def hide_scroll(app, args):
    app.page.show_scroll(False)

def show_scroll(app, args):
    app.page.show_scroll(True)

def scroll(app, args):
    if len(args) > 0:
        match args[0]:
            case "1":
                app.page.show_scroll(True)
            case "0":
                app.page.show_scroll(False)
            case _:
                print("Valid arguments for the scroll command are 0 or 1")


def scale(app, args):
    if len(args) > 0:
        if args[0] == "reset":
            app.resize_manual(320, 240)
        else:
            try:
                _scale = abs(float(args[0]))
                app.resize_manual(int(app.width*_scale), int(app.height*_scale))
            except:
                print(f"{args[0]} is not a valid argument. Please use a number > 0 or reset")



commands = {
    "scroll" : scroll,
    "scale" : scale
}

descriptions = {
    "scroll" : "shows and hides scrollbar (scroll 0..1)",
    "scale" :  "scales the screen by a factor or reset to original dimensions"
}