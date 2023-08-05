import subprocess
import streamlit as st

def change_dir(dir_path):
    command = "cd " + dir_path
    subprocess.run(["powershell", "-Command", command], shell=True)

def download_audio(youtube_url):
    command = f"yt-dlp --embed-thumbnail -x --audio-format mp3 {youtube_url}"
    subprocess.run(["powershell", "-Command", command], shell=True)

def filter_url_link(url):
    # remove the playlist part of the url
    if "&list=" in url:
        url = url[:url.index("&list=")]
    # remove the time part of the url
    if "&t=" in url:
        url = url[:url.index("&t=")]
    # remove the channel part of the url
    if "&ab_channel=" in url:
        url = url[:url.index("&ab_channel=")]
    return url


def main():
    st.title("YouTube Audio Downloader")

    # important note
    st.write("Note: This app uses yt-dlp, a YouTube downloader. You have to have it installed first in your computer")
    
    st.write("Enter the YouTube video URL:")
    youtube_url = st.text_input("URL", "")

    st.write("Enter the directory to save the audio file:")
    dir_path = st.text_input("Directory", "")

    if st.button("Download Audio"):
        if youtube_url:
            st.write("Downloading audio...")
            change_dir(dir_path)
            filtered_url = filter_url_link(youtube_url)
            download_audio(filtered_url)
            st.success("Download completed.")
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    main()
