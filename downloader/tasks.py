from celery import shared_task
from downloader.utils.video import download_video
from downloader.models import Archive

@shared_task
def video_task(archive_id):
    Archive.status = Archive.StatusChoice.PENDENTE
    print("Status", Archive.status)
    try:
        download_video(archive_id)
        Archive.status = Archive.StatusChoice.CONCLUIDO
        print("Status", Archive.status)
    except Exception as e:
        Archive.status = Archive.StatusChoice.FALHA
        print("Status", Archive.status)
        raise ValueError("Erro ao baixar vídeo:", e)