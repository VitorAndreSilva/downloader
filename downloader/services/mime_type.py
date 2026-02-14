from downloader.models import Archive
from downloader.utils.fill_type import fill_type
import mimetypes

def mime_type(instance: Archive):
    mime, encoding = mimetypes.guess_type(instance.url, strict=True)
    if mime:
        if mime.startswith('video'):
            instance.type = instance.TypeChoices.VIDEO
        #elif mime.startswith('image') or mime.startswith('text') or mime.startswith('application'):
        else:
            instance.type = instance.TypeChoices.ARCHIVE
    else:
        fill_type(instance)
    print(instance.type)
    return instance.type