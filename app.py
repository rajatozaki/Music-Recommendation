import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

CLIENT_ID = "your_id"
CLIENT_SECRET = "your_id"

def init_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_details(song_name, artist_name):
    sp = init_spotify_client()
    try:
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track")
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            album_cover_url = track['album']['images'][0]['url']
            spotify_url = track['external_urls']['spotify']  # Fetch the Spotify URL
            return album_cover_url, spotify_url
        else:
            default_image = "https://i.postimg.cc/0QNxYz4V/social.png"
            return default_image, None
    except Exception as e:
        st.error(f"Error fetching song details: {e}")
        return "https://i.postimg.cc/0QNxYz4V/social.png", None

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names, recommended_music_posters, spotify_urls = [], [], []
    for i in distances[1:11]:  # Get top 10 recommendations
        artist = music.iloc[i[0]].artist
        song_title = music.iloc[i[0]].song
        album_cover_url, spotify_url = get_song_details(song_title, artist)
        recommended_music_posters.append(album_cover_url)
        recommended_music_names.append(song_title)
        spotify_urls.append(spotify_url)
    return recommended_music_names, recommended_music_posters, spotify_urls

# Load data
music = pd.read_csv(r'C:\Users\Rajat Saini\music.csv')
similarity = np.load(r'C:\Users\Rajat Saini\similarity.npy')

# Sidebar menu with app description
st.sidebar.title("Music Recommender Description")

st.sidebar.subheader("Techniques Utilized")

st.sidebar.markdown("**Cosine Similarity:**")
st.sidebar.markdown("- Determines similarity between songs based on TF-IDF vectors derived from song lyrics.")
st.sidebar.markdown("- TF-IDF vectorization transforms text data into a numeric format, facilitating effective recommendation.")

st.sidebar.markdown("**TF-IDF Vectorization:**")
st.sidebar.markdown("- Transforms raw text (song lyrics) into a structured format suitable for machine learning algorithms.")
st.sidebar.markdown("- Reflects the importance of terms in a document relative to others, aiding in recommendation.")

# Main content
st.title('Music Recommender')

selected_song = st.selectbox("Select a song from the dropdown", music['song'].values)

if st.button('Show Recommendations'):
    recommended_music_names, recommended_music_posters, spotify_urls = recommend(selected_song)
    # Create two rows of 5 columns each for recommendations
    for j in range(2):  # Two rows
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                pos = 5 * j + idx  # Calculate position in list
                if spotify_urls[pos]:  # Ensure the URL is not None
                    st.markdown(f"[{recommended_music_names[pos]}]({spotify_urls[pos]})")
                else:
                    st.text(recommended_music_names[pos])  # Fallback to text if no URL
                st.image(recommended_music_posters[pos])
