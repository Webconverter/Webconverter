from django.db import models
from django.forms import ModelForm
import os


# Create your models here.

class Upload(models.Model):
	pic = models.ImageField("Image", upload_to="images/")
	upload_date=models.DateTimeField(auto_now_add = True)


class UploadForm(ModelForm):
	class Meta:
		model = Upload
