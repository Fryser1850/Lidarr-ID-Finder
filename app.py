import streamlit as st
import musicbrainzngs
import locale

# --- CONFIGURATION ---
APP_NAME = "Lidarr-ID-Finder"
VERSION = "1.0"
# Standard Practice: The repo URL is the default contact info
REPO_URL = "https://github.com/Fryser1850/Lidarr-ID-Finder"

st.set_page_config(page_title=APP_NAME, page_icon="🎵")

# --- LOCALIZATION (English & French) ---
TEXTS = {
    "en": {
        "title": f"🎵 {APP_NAME}",
        "subtitle": "Find the MusicBrainz ID for manual import into Lidarr.",
        "search_label": "Artist Name:",
        "placeholder": "Ex: Daft Punk",
        "loading": "Searching MusicBrainz...",
        "no_result": "No results found.",
        "results_found": "results found.",
        "desc": "Description",
        "genres": "Genres",
        "copy_text": "👇 Copy this ID for Lidarr:",
        "error": "An error occurred:",
        "footer": "Data provided by MusicBrainz API."
    },
    "fr": {
        "title": f"🎵 {APP_NAME}",
        "subtitle": "Trouve l'ID MusicBrainz pour l'import manuel dans Lidarr.",
        "search_label": "Nom de l'artiste :",
        "placeholder": "Ex: Daft Punk",
        "loading": "Recherche sur MusicBrainz...",
        "no_result": "Aucun résultat trouvé.",
        "results_found": "résultats trouvés.",
        "desc": "Description",
        "genres": "Genres",
        "copy_text": "👇 Copier cet ID pour Lidarr :",
        "error": "Une erreur est survenue :",
        "footer": "Données fournies par MusicBrainz API."
    }
}

# --- AUTO-DETECT LANGUAGE ---
try:
    system_locale = locale.getdefaultlocale()[0]
    # Default to English (0) unless French is detected
    default_index = 1 if system_locale and 'fr' in system_locale.lower() else 0
except:
    default_index = 0

# --- HEADER & LANGUAGE SELECTOR ---
col_title, col_lang = st.columns([5, 1])
with col_lang:
    selected_lang = st.selectbox(
        "Language", 
        ["en", "fr"], 
        index=default_index, 
        label_visibility="collapsed"
    )

t = TEXTS[selected_lang]

with col_title:
    st.title(t["title"])

st.write(t["subtitle"])

# --- SAFE API LOGIC ---
# Standard Open Source Logic:
# 1. Try to get custom contact from secrets
# 2. If secrets file is missing (FileNotFound) or key is missing, fallback to REPO_URL
try:
    contact_info = st.secrets["mb_contact"]
except Exception:
    # This block runs if .streamlit/secrets.toml does not exist
    contact_info = REPO_URL

musicbrainzngs.set_useragent(APP_NAME, VERSION, contact_info)

# --- SEARCH LOGIC ---
query = st.text_input(t["search_label"], placeholder=t["placeholder"])

if query:
    with st.spinner(t["loading"]):
        try:
            # Query MusicBrainz API
            result = musicbrainzngs.search_artists(artist=query, limit=10)
            artist_list = result['artist-list']
            
            if not artist_list:
                st.warning(t["no_result"])
            else:
                st.success(f"{len(artist_list)} {t['results_found']}")
                
                for artist in artist_list:
                    # Extract Data safely
                    name = artist.get('name', 'Unknown')
                    mbid = artist.get('id', '')
                    country = artist.get('country', 'N/A')
                    score = artist.get('ext:score', '0')
                    desc = artist.get('disambiguation', '-')
                    
                    # Extract Tags (Genres)
                    tags = artist.get('tag-list', [])
                    tags_str = ", ".join([tag['name'] for tag in tags[:5]]) if tags else "-"
                    
                    # Display Results
                    with st.expander(f"**{name}** ({country}) - Score: {score}%"):
                        st.write(f"**{t['desc']}** : {desc}")
                        st.write(f"**{t['genres']}** : {tags_str}")
                        st.markdown("---")
                        st.caption(t["copy_text"])
                        st.code(f"lidarr:{mbid}", language="text")

        except Exception as e:
            st.error(f"{t['error']} {e}")

st.markdown("---")
st.caption(t["footer"])