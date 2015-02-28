from PIL import Image
from django.conf import settings

def image(curr_file, wntd_file):
	curr_file_path = str(settings.MEDIA_ROOT) + '/images/' + curr_file
	new_file = ''.join(curr_file_path.split('.')[:-1])
	out_file = new_file + wntd_file
	im = Image.open(curr_file_path).save(out_file)
	return im

