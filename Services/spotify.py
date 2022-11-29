import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-follow-read," \
        "user-library-read," \
        "user-library-modify," \
        "user-modify-playback-state," \
        "user-read-playback-state," \
        "user-read-currently-playing," \
        "app-remote-control," \
        "playlist-read-private," \
        "playlist-read-collaborative," \
        "playlist-modify-public," \
        "playlist-modify-private," \
        "streaming"

class Spotify:

    def __init__(self, clientid, clientsecret, redirecturi ):
        # Setup authentication
        temp_auth = SpotifyOAuth(clientid, clientsecret, redirecturi, scope=SCOPE, cache_path='cache')
        self.sp = spotipy.Spotify(auth_manager=temp_auth)

    # Singleton manager
    def __new__(cls):
        if cls._instance is None:
          cls._instance = super(Spotify, cls).__new__(cls)
        return cls._instance

    def refresh_devices(self):
        results = self.sp.devices()
        print(results)
        #for _, item in enumerate(results['devices']):
        #        print(item['name'])
        #        device = UserDevice(item['id'], item['name'], item['is_active'])
        #        DATASTORE.setUserDevice(device)

        
    # MEDIA CONTROLS
    def next(self):
        self.sp.next_track()

    def previous(self):
        self.sp.previous_track()