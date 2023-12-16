# THIS REPOSITORY IS CURRENTLY UNFINISHED

# Spotify-Playlist-Sort-Program
This program uses Spotipy for a user's existing playlist to create a new playlist sorted alphabetically by artist. As well as this, it then sorts by album release date and track listing.


# guide

1. Download or copy the code.

2. Make sure your IDE has Pycharm and can import Spotipy.

3. Enter your details (see 'Required Information').

4. run program.


# Required Information
In order for you to find much of the information you need for this program to work, you will need to go to https://developer.spotify.com/ and create a new 'App'.

'client_ID' - This can be found in the 'Basic Information' part of your settings within your App.
![image](https://github.com/blueberry2345/Spotify-Playlist-Sort-Program/assets/102472091/f5b1321f-a00c-4082-91f0-72cfccc741fe)


'client_secret' - can be found by pressing the link below the Client ID      
![image](https://github.com/blueberry2345/Spotify-Playlist-Sort-Program/assets/102472091/cb35d931-64c2-4bfb-b954-1f5a368dc6e8)



'redirect_uri' (Changing this is optional) - This is where you are redirected after the authorisation. I have set it as 'http://localhost:8888/callback' but this can be changed if you have a preference. Make sure your 'redirect_uri' will be consistent with the value of 'Redirect URIs' on your Spotify Developer app.
![image](https://github.com/blueberry2345/Spotify-Playlist-Sort-Program-SPx2/assets/102472091/c3ce0703-9d3d-4e0a-be4e-2fc6b5e1d146)


, 'scopes', 'playlist_id' and 'user_id' 
