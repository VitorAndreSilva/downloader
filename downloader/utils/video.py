import yt_dlp
import os
from config import settings
from django.core.files import File

output_directory = os.path.join(settings.MEDIA_ROOT, 'downloads')
os.makedirs(output_directory, exist_ok=True)

def download_video(url, instance):
    ydl_opts = {
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) *continua*",
            "Accept-Language": "pt-BR,pt;q=0.9",
        },
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        with open(filename, 'rb') as file:
            instance.archive.save(os.path.basename(filename), File(file))
        
        return instance.archive.url
            
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        raise ValueError("Erro ao baixar o arquivo")