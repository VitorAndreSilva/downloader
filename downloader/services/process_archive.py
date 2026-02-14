from downloader.models import Archive
from downloader.tasks import video_task
from downloader.utils.archive import download_archive

def process_archive(instance: Archive):
    if instance.type == instance.TypeChoices.VIDEO:
        video_task.delay(instance.id)
    else:
        download_archive(instance.url, instance)