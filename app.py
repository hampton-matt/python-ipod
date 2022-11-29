from Services.spotify import Spotify
import settings

sp = Spotify(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI)

sp.refresh_devices()