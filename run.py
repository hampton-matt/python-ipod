#from Services.spotify import Spotify
import settings

#sp = Spotify(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI)

#sp.refresh_devices()

# Check program is being run from here
if __name__ != "__main__":
    exit()

from Debugging.debugger import debugging
from Frontend.app import App
from Interaction.keyboard import interact

def onKeyPress(event):
    c = event.keycode
    interact(c, None)




app = App(320, 240, "default")

app.bind("<Configure>", app.resize)
app.bind('<KeyPress>', onKeyPress)
app.after(1000, debugging(app))
app.mainloop()