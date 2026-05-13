import streamlit as st  # type: ignore
import pandas as pd  # type: ignore

# Load the dataset
csv_file_path = 'spotify_top_music.csv'
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    st.error(f"Error: The file '{csv_file_path}' was not found. Please ensure it's uploaded.")
    st.stop()

st.title('Spotify Top Music Explorer')
st.write('Select a song to see its details:')

# Get unique song titles for the dropdown
song_titles = df['title'].unique()
song_titles.sort() # Sort titles alphabetically

selected_song = st.selectbox(
    'Choose a song:',
    song_titles
)

if selected_song:
    song_info = df[df['title'] == selected_song]
    
    if not song_info.empty:
        st.subheader(f'Details for: {selected_song}')
        # Display all columns for the selected song
        for col in song_info.columns:
            st.write(f"**{col.replace('_', ' ').title()}:** {song_info[col].iloc[0]}")
    else:
        st.write('Song not found in the dataset.')