from PIL import Image
from django.conf import settings


supported = ['.jpg', '.png']

def image(curr_file, wntd_file):
    ext = '.' + curr_file.split('.')[-1]
    if ext in supported:
	    wntd_file = wntd_file.lower()
	    curr_file_path = str(settings.MEDIA_ROOT) + 'images/' + curr_file
	    list_path = curr_file_path.split('.')[:-1]
	    new_path = str(list_path[0])+ '.' + wntd_file
	    print(ext)
	    Image.open(curr_file_path).save(new_path)
	    return curr_file
    else:
	    return 'not supported'


 
