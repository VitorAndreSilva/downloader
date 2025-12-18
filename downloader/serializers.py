from rest_framework import serializers
from downloader.models import Archive

class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'
        read_only_fields = ['user']