# Music-Recommendation
This is a Streamlit web application for recommending music based on song lyrics using natural language processing (NLP) techniques. The app utilizes Spotify's API for fetching song details and generates recommendations based on cosine similarity calculated from TF-IDF vectors derived from song lyrics.

**Features**
Select a song from the dropdown menu.
Click on "Show Recommendations" to display 10-15 recommended songs based on similarity to the selected song.
Each recommendation includes the song title and album cover image, with clickable links to open the song on Spotify.

**Technologies Used**
Streamlit: Python library for creating interactive web apps.
Spotipy: Python library for interacting with Spotify's Web API.
pandas: Python library for data manipulation and analysis.
numpy: Python library for numerical computing.
scikit-learn: Python library for machine learning.
GitHub: Platform for hosting the repository and version control.

Installation
Clone the repository:
git clone https://github.com/rajatozaki/Music-Recommendation.git

Run the Streamlit app:
streamlit run app.py


Data Sources
Kaggle Dataset: Spotify Million Song Dataset: Used for song metadata and lyrics.
Preprocessed lyrics data and similarity matrix.
