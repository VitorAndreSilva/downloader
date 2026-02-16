from celery import shared_task
from downloader.utils.video import download_video
from downloader.models import Archive

@shared_task
def video_task(archive_id):
    try:
        download_video(archive_id)

    except Exception as e:
        raise ValueError("Erro ao baixar vídeo:", e)