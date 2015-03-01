from PIL import Image
from django.conf import settings
import os

def image(curr_file, wntd_file):
    wntd_file = wntd_file.lower()
    curr_file_path = str(settings.MEDIA_ROOT) + 'images/' + curr_file
    list_path = curr_file_path.split('.')[:-1]
    new_path = str(list_path[0])+ '.' + wntd_file
    print(new_path, curr_file_path)
    Image.open(curr_file_path).save(new_path)
    return os.path.abspath(new_path)


 
