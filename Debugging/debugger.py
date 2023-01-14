import Debugging.frontend as frontend

descriptions = {
    "help" : "prints a list of commands",
    "exit" : "closes the application",
}

def exit(app, args):
    app.destroy()

def help(app, args):
    print("\nHelp:")
    for c in descriptions:
        tabs = "\t"
        if len(c) < 5:
            tabs = "\t\t"
        print(f"   {c}{tabs}{descriptions.get(c)}")

    print("\nFrontend Commands:")
    for c in frontend.descriptions:
        tabs = "\t"
        if len(c) < 5:
            tabs = "\t\t"
        print(f"   {c}{tabs}{frontend.descriptions.get(c)}")


commands = {
    "help" : help,
    "exit" : exit,
}
for c in frontend.commands:
    commands[c] = frontend.commands.get(c)

def console_input(app):
    _input = input("python-iPod >> ")
    _split = _input.split(" ")
    _args = None
    _func = commands.get(_split[0])
    
    if len(_split) > 1:
        list.pop(_split, 0)
        _args = _split
    if _func is not None:
        _func(app, _args)
    else:
        print(f"\'{_input}\' is not a recognised command\nRun \'help\' to see a list of commands")

def debugging(app):
    def function():
        app.refresh()
        console_input(app)
        app.after(100, function)
    return function