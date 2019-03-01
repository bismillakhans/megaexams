from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField,ModificationDateTimeField
#import pytesseract
import json
import base64
import requests
#from PIL import Image, ImageEnhance, ImageFilter


# Create your models here.
class Ques(models.Model):
    title=models.CharField(max_length=70 ,blank=True)
    img = models.ImageField(upload_to='images')
    verify_date = ModificationDateTimeField()
    corrected_date = ModificationDateTimeField()
    text=models.TextField(max_length=1000 ,blank=True)
    ocrtext=models.TextField(max_length=1000 ,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    #ocrstatus=models.BooleanField(default=False,verbose_name="ocr_genereted")
    status = models.BooleanField(default=True, verbose_name="Approve")
    verify = models.BooleanField(default=False, verbose_name="verify")
    corrected = models.BooleanField(default=False, verbose_name="corrected")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exams:update', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if self.img :
            
    
            im = Image.open(self.img)
            im = im.convert('L')                             # grayscale
            im = im.filter(ImageFilter.MedianFilter())       # a little blur
            im = im.point(lambda x: 0 if x < 140 else 255)
            self.ocrtext = pytesseract.image_to_string(im)
            
        if self.status:
            if not self.corrected:
                self.text=self.ocrtext
        super(Ques, self).save(*args, **kwargs)


    

