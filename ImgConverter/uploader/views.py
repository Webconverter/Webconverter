from django.test import TestCase
from django.shortcuts import render
from uploader.models import UploadForm, Upload
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from uploader.convert import image

# Create your tests here.
def home(request):
    if request.method == 'POST':
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            wantedFormat = str(request.POST.get("select_box"))
            name = str(request.FILES['pic'])
            location = image(name, wantedFormat)
            print(location)
            return render(request, 'convert.html',{ 'newimage':location})		
    else:
        img = UploadForm()
    images = Upload.objects.all()
    return render(request, 'home.html',{'form':img,'images':images})		


		
	


