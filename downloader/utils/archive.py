import requests, os
from config import settings
from urllib.parse import urlparse
from django.core.files import File
from downloader.models import Archive

def download_archive(url, instance: Archive):
    # Requisita o arquivo
    response = requests.get(url, stream=True, verify=False)
    # Dá o caminho do arquivo
    output_directory = os.path.join(settings.MEDIA_ROOT, 'downloads')
    os.makedirs(output_directory, exist_ok=True)
    # Dá nome e tipo correto ao arquivo
    header = response.headers.get("Content-Disposition")
    path = None
    if header and "filename=" in header:
        path = header.split("filename=")[1].strip('"') # Se o tipo correto estiver no header
    if not path:
        parsed = urlparse(url)
        path = os.path.basename(parsed.path) # Pega o nome do arquivo pela URL
    if not path:
        path = f'{instance.name}.bin' # Arquivo binário
    # Muda o status
    instance.status = instance.StatusChoice.PENDENTE
    instance.save(update_fields=["status"])
    print("Status", instance.status)
    # Salva o arquivo
    try:
        with open(os.path.join(output_directory, path), 'wb') as file:
            file.write(response.content)
            print("Arquivo baixado com sucesso: ", file)
        with open(os.path.join(output_directory, path), 'rb') as file:
            instance.archive.save(path, File(file))
        instance.status = instance.StatusChoice.CONCLUIDO
        print("Status", instance.status)
        instance.save()
        return instance.archive.url
    except Exception as e:
        instance.status = instance.StatusChoice.FALHA
        instance.save(update_fields=["status"])
        print("Download sem sucesso:", e)
        print("Status", instance.status)