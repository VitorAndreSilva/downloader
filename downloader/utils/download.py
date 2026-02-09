from django.http import FileResponse, Http404
from downloader.models import Archive
import mimetypes

def download_archive(request, pk):
    archive = Archive.objects.get(pk=pk, user=request.user)
    if archive.archive:
        mime_type, _ = mimetypes.guess_type(archive.archive.path)
        response = FileResponse(
            open(archive.archive.path, 'rb'),
            content_type=mime_type or 'application/octet-stream'
            )
        response['Content-Disposition'] = f'attachment; filename="{archive.name}"'
        return response
    else:
        raise Http404("Vídeo não encontrado")