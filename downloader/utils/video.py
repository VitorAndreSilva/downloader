#from downloader.models import Archive
import yt_dlp
import os

output_directory = os.path.join(os.path.expanduser("~"), "Downloads")
os.makedirs(output_directory, exist_ok=True)

def download_video(url, instance=None):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download concluído!")
            return url
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            raise ValueError("Erro ao baixar o arquivo")