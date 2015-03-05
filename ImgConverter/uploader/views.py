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
            img.save("test")
            wantedFormat = request.POST.get("select_box")
            name = str(request.FILES['pic'])
            x = request.POST.get("x_value")
            y = request.POST.get("y_value")
            rot = request.POST.get("deg_value")
            message = image(name, wantedFormat, x, y, rot)
            if message == 'not supported':
                return render(request, 'home.html', {'form':img, 'newimage': message}) 
            return render(request,'home.html',{'form':img, 'newimage':message})
    else:
        img = UploadForm()
    return render(request, 'home.html',{'form':img})
