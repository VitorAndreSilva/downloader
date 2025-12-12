import requests, os
from urllib.parse import urlparse

def download_archive(url, instance):
    # Requisita o arquivo
    response = requests.get(url, stream=True)
    # Dá o caminho do arquivo
    output_directory = os.path.join(os.path.expanduser("~"), "Downloads")
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
            return file
    except Exception as e:
        print("Download sem sucesso:", e)