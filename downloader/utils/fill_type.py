from downloader.models import Archive
from urllib.parse import urlparse

ARCHIVE_EXTENSIONS = (
    ".pdf", ".jpg", ".jpeg", ".png", ".gif",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".txt", ".csv", ".xlsx", ".xls", ".doc", ".docx",
    ".mp3", ".wav", ".flac",
    ".iso", ".bin", ".hex", ".exe", ".msi", ".json", ".svg",
    ".iso", ".docx"
)

def fill_type(instance: Archive):
        if "youtube" in instance.url or "vimeo" in instance.url or "youtu.be" in instance.url:
            instance.type = instance.TypeChoices.VIDEO
            print(instance.type)
            return instance.type
        path = urlparse(instance.url).path.lower()
        for ext in ARCHIVE_EXTENSIONS:
            if ext in path:
                instance.type = instance.TypeChoices.ARCHIVE
                print(instance.type)
                return instance.type
        instance.type = instance.TypeChoices.GENERIC
        print(instance.type)
        return instance.type