import subprocess

def download_youtube(url, audio_only=False):
    try:
        if audio_only:
            # Download best audio and convert to mp3
            cmd = [
                "yt-dlp",
                "-x",
                "--audio-format", "mp3",
                url
            ]
        else:
            # Download best video + audio
            cmd = [
                "yt-dlp",
                "-f", "bestvideo+bestaudio/best",
                url
            ]

        subprocess.run(cmd, shell=True)
        print("✅ Download complete!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    choice = input("Download as (v)ideo or (a)udio? ").strip().lower()
    audio = choice == 'a'
    download_youtube(url, audio_only=audio)

