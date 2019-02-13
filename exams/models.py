from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


# Create your models here.
class Ques(models.Model):
    title=models.CharField(max_length=70)
    slug=AutoSlugField(populate_from='title', overwrite=True)
    img = models.ImageField(upload_to='images')
    text=models.CharField(max_length=70,blank=True)
    ocrtext=models.CharField(max_length=70,blank=True)
    post_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True, verbose_name="Approve")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exams:update', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if self.img:
            im = Image.open(self.img)
            im = im.convert('L')                             # grayscale
            im = im.filter(ImageFilter.MedianFilter())       # a little blur
            im = im.point(lambda x: 0 if x < 140 else 255)
            self.ocrtext = pytesseract.image_to_string(im)
        super(Ques, self).save(*args, **kwargs)


    

