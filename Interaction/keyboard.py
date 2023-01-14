def default(page):
    print("worked")


KEYS = {
    2113992448: default,                    # UP
    2097215233: default,                    # DOWN
    2063660802: default,                    # LEFT (MENU)
    2080438019: default,                    # RIGHT (SELECT)
    201326705: default,                     # PREV
    234881125: default,                     # NEXT
    822083616: default                      # PLAY
}

def interact(keycode, page):
    if keycode in KEYS:
        KEYS[keycode](page)