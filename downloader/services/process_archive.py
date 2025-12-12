from downloader.models import Archive
from downloader.utils.video import download_video
from downloader.utils.archive import download_archive
from downloader.utils.generic import download_generic

def process_archive(instance: Archive):
    if instance.type == instance.TypeChoices.VIDEO:
        download_video(instance.url, instance=None)
    elif instance.type == instance.TypeChoices.ARCHIVE:
        download_archive(instance.url, instance)
    else:
        download_generic(instance.url, instance)