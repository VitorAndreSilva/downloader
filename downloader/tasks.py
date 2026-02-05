from celery import shared_task
from downloader.utils.video import download_video

@shared_task
def video_task(archive_id):
    download_video(archive_id)