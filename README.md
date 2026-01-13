# 🎵 Lidarr-ID-Finder

A simple Streamlit tool to help you find the correct **MusicBrainz ID** for artists and easily import them into **Lidarr**.

This tool is useful when Lidarr's internal search fails to find specific artists and their ID.

## Features
* 🔍 **Direct Search**: Queries the MusicBrainz API directly.
* 🌍 **Internationalization**: The app support **English** and **French** 
* 📋 **One-click Copy**: Generates the `lidarr:mbid` format, ready to paste into Lidarr's search bar.

## 🚀 How to Run

**Prerequisites:** Python 3.8+

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Fryser1850/Lidarr-ID-Finder.git
    cd Lidarr-ID-Finder
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```

## ⚙️ Configuration (Optional)

By default, the app uses this repository's URL as the User-Agent contact for the MusicBrainz API.
If you plan to use this tool heavily, please configure your own email to avoid shared rate-limiting.

1. Create a folder named `.streamlit` in the project root.
2. Create a file named `secrets.toml` inside it.
3. Add your email:
   ```toml
   mb_contact = "your-email@example.com"

⚠️ Disclaimer & Contributing
I am not a professional developer. This project was entirely generated using Artificial Intelligence (Google Gemini) to solve a personal need. While it works for me, the code might contain errors, inefficiencies, or non-standard practices.

Contributions are highly encouraged! If you are a developer, please feel free to:

Fork the repository

Refactor the code

Fix bugs or add new features

Submit a Pull Request

The goal is to make this tool useful for the entire self-hosted community.

License
MIT License
