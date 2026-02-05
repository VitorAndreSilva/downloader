from downloader.models import Archive
from downloader.tasks import video_task
from downloader.utils.archive import download_archive
from downloader.utils.generic import download_generic

def process_archive(instance: Archive):
    if instance.type == instance.TypeChoices.VIDEO:
        video_task.delay(instance.id)
    elif instance.type == instance.TypeChoices.ARCHIVE:
        download_archive(instance.url, instance)
    else:
        download_generic(instance.url, instance)