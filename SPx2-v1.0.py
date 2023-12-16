import spotipy

# input your details for these variables. Go to the 'README' for more information about this
client_ID = ""
client_secret = ""
redirect_uri = "http://localhost:8888/callback"
scopes = "playlist-modify-private playlist-read-private playlist-modify-public"
playlist_link = ""
user_id = ""
#creation of two lists. one for the track order of the current playlist and the other for the new playlist
tracks = []
sorted_tracks = []


# creation of class 'Track' that stores relevant information about a track in the playlist
class Track:
    def __init__(self, artist, release_date_y, release_date_m, release_date_d, album, track_no, uri):
        self.artist = artist
        self.album = album
        self.track_number = track_no
        self.year = release_date_y
        self.month = release_date_m
        self.day = release_date_d
        self.uri = uri


#authenticate use of Spotify account
authorisation_class = spotipy.oauth2.SpotifyOAuth(client_id=client_ID, client_secret=client_secret,
                                                  redirect_uri=redirect_uri, scope=scopes, cache_path="./tokens.txt",
                                                  show_dialog=True)
session = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=client_ID, client_secret=client_secret,
                                                                   redirect_uri=redirect_uri, scope=scopes,
                                                                   cache_path="tokens.txt", show_dialog=True))
# gather information about the playlist itself
playlist = session.user_playlist(user_id, playlist_id)
playlist_name = session.user_playlist(user_id, playlist_id)['name']
playlist_public = playlist['public']

#create a new track object for each item on the spotify playlist
for song in playlist['tracks']['items']:
    tracks.append(Track(song['track']['artists'][0]['name'], song['track']['album']['release_date'][:4],
                        song['track']['album']['release_date'][6:7], song['track']['album']['release_date'][9:10],
                        song['track']['album']['name'], song['track']['track_number'], song['track']['uri']))

#sort tracks by artist then by date, album and track listing
tracks = sorted(tracks, key=lambda x: (x.artist, x.year, x.month, x.day, x.album, x.track_number))

#add the track uri to a list of tracks
for track in tracks:
    sorted_tracks.append({track.uri})

# new playlist is created
playlist = session.user_playlist_create(user=user_id, name=playlist_name, public=playlist_public, description="")
print(playlist['id'])

#add tracks to new playlist by using the uri of each track in the sorted list
for track in sorted_tracks:
    session.playlist_add_items(playlist_id=playlist['id'], items=track)

