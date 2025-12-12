from rest_framework import viewsets
from downloader.models import Archive
from downloader.serializers import ArchiveSerializer
from downloader.services.process_archive import process_archive
from downloader.services.mime_type import mime_type

class DownloaderViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        print("Instância salva: ", instance)
        mime_type(instance)
        process_archive(instance)
        instance.save()