class UserDevice():
    __slots__ = ['id', 'name', 'is_active']
    def __init__(self, id, name, is_active):
        self.id = id
        self.name = name
        self.is_active = is_active

class UserTrack():
    __slots__ = ['title', 'artist', 'album', 'uri']
    def __init__(self, title, artist, album, uri):
        self.title = title
        self.artist = artist
        self.album = album
        self.uri = uri

    def __str__(self):
        return self.title + " - " + self.artist + " - " + self.album

class UserAlbum():
    __slots__ = ['name', 'artist', 'track_count', 'uri']
    def __init__(self, name, artist, track_count, uri):
        self.name = name
        self.artist = artist
        self.uri = uri
        self.track_count = track_count

    def __str__(self):
        return self.name + " - " + self.artist

class UserArtist():
    __slots__ = ['name', 'uri']
    def __init__(self, name, uri):
        self.name = name
        self.uri = uri

    def __str__(self):
        return self.name

class UserPlaylist(): 
    __slots__ = ['name', 'idx', 'uri', 'track_count']
    def __init__(self, name, idx, uri, track_count):
        self.name = name
        self.idx = idx
        self.uri = uri
        self.track_count = track_count

    def __str__(self):
        return self.name

class SearchResults():
    __slots__ = ['tracks', 'artists', 'albums', 'album_track_map']
    def __init__(self, tracks, artists, albums, album_track_map):
        self.tracks = tracks
        self.artists = artists
        self.albums = albums
        self.album_track_map = album_track_map