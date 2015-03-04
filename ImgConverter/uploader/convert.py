from PIL import Image
from django.conf import settings
import re


supported = ['.jpg', '.png','.bmp', '.tiff']

def image(curr_file, wntd_file, x, y):
    ext = '.' + curr_file.split('.')[-1]
    curr_file = re.sub('[%]', '', curr_file).replace(' ', '_')
    if ext in supported:
        curr_file_path = str(settings.MEDIA_ROOT) + 'images/' + curr_file
        new_path = str(curr_file_path.split('.')[:-1][0])+ '.' + wntd_file
        im = Image.open(curr_file_path)
        try:
            x = int(x)
            y = int(y)
            im.resize((x, y)).save(new_path)
            print("heloe", x, y)
        except:
            Image.open(curr_file_path).save(new_path)
        return 'images/' + new_path.split('/')[-1]
    else:
        return 'sorry not supported'
