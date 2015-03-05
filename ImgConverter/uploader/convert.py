from PIL import Image
from django.conf import settings
import re


supported = ['.jpg', '.png','.bmp', '.tiff']

def image(curr_file, wntd_file, x, y, rot):
    """
    image covert function. Takes current file path, wanted file ending and optional x and y paramenters.
    """
    ext = '.' + curr_file.split('.')[-1]
    curr_file = re.sub('[%]', '', curr_file).replace(' ', '_') #use a regex sub to remove invalid characters
    if ext in supported:
        curr_file_path = str(settings.MEDIA_ROOT) + 'images/' + curr_file
        new_path = str(curr_file_path.split('.')[:-1][0])+ '.' + wntd_file
        im = Image.open(curr_file_path)
        try:
            print("halle")
            x = int(x)
            y = int(y)
            im.resize((x,y)).save(curr_file_path)
        except:
            pass
        try:
            rot = int(rot)
            if rot != 0:
                im.rotate(rot).save(curr_file_path)
        except:
            pass
        print(x, y, rot)
        im.save(new_path)
        return 'images/' + new_path.split('/')[-1]
    else:
        return 'sorry not supported'
