from downloader.models import Archive

def fill_type(instance: Archive):
        if "youtube" in instance.url or "vimeo" in instance.url or "youtu.be" in instance.url:
            instance.type = instance.TypeChoices.VIDEO
            print(instance.type)
            return instance.type
        #path = urlparse(instance.url).path.lower()
        #for ext in ARCHIVE_EXTENSIONS:
            #if ext in path:
                #instance.type = instance.TypeChoices.ARCHIVE
                #print(instance.type)
                #return instance.type
        else:
            instance.type = instance.TypeChoices.ARCHIVE
            print(instance.type)
            return instance.type