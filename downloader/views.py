from rest_framework import viewsets
from downloader.models import Archive
from downloader.serializers import ArchiveSerializer
from downloader.services.process_archive import process_archive
from downloader.services.mime_type import mime_type
from rest_framework.permissions import IsAuthenticated

class DownloaderViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.none()
    serializer_class = ArchiveSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        print("Instância salva: ", instance)
        mime_type(instance)
        process_archive(instance)
        instance.save()
    def get_queryset(self):
        return Archive.objects.filter(user=self.request.user)