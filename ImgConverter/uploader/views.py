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
            message = image(name, wantedFormat)
            if message == 'not supported':
                return render(request, 'home.html', {'form':img, 'message': message}) 
            return render(request, 'home.html',{ 'newimage':message})
    else:
        img = UploadForm()
    return render(request, 'home.html',{'form':img})
