import requests, os
from config import settings
from urllib.parse import urlparse
from django.core.files import File

def download_archive(url, instance):
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
    # Salva o arquivo
    try:
        with open(os.path.join(output_directory, path), 'wb') as file:
            file.write(response.content)
            print("Arquivo baixado com sucesso: ", file)
        with open(os.path.join(output_directory, path), 'rb') as file:
            instance.archive.save(path, File(file))
        
        instance.save()
        return instance.archive.url
    except Exception as e:
        print("Download sem sucesso:", e)