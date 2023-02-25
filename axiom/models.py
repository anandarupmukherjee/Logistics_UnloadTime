from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File


import random
class QrCode(models.Model):
    url=models.URLField()
    image=models.ImageField(upload_to='qrcode',blank=True)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image001.png',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

# Create your models here.
#class Project(models.Model):
#	timestamp=models.TextField()
#	order_id=models.TextField()
#	container=models.TextField()
#	time_in=models.TextField()
#	time_out=models.TextField()
#	worker=models.TextField()


class Project(models.Model):
        timestamp=models.TextField()
        order_id=models.TextField()
        container=models.TextField()
        date_work=models.TextField(default='')
        time_in=models.TextField()
        time_out=models.TextField()
        w1_start=models.TextField()
        w2_start=models.TextField()
        w3_start=models.TextField()
        w4_start=models.TextField()
        w5_start=models.TextField()
        w1_stop=models.TextField()
        w2_stop=models.TextField()
        w3_stop=models.TextField()
        w4_stop=models.TextField()
        w5_stop=models.TextField()
        w1_break_on=models.TextField()
        w1_break_off=models.TextField()
        w2_break_on=models.TextField()
        w2_break_off=models.TextField()
        w3_break_on=models.TextField()
        w3_break_off=models.TextField()
        w4_break_on=models.TextField()
        w4_break_off=models.TextField()
        w5_break_on=models.TextField()
        w5_break_off=models.TextField()
        supervisor=models.TextField()
        customer=models.TextField()
        product=models.TextField()
        packages=models.TextField()
        sku=models.TextField()
        size=models.TextField()



class Project_buffer(models.Model):
        order_id=models.TextField()
        container=models.TextField()
        unload_time=models.TextField()
        workers=models.TextField()
        w1=models.TextField()
        w2=models.TextField()
        w3=models.TextField()
        w4=models.TextField()
        w5=models.TextField()
        tw=models.TextField()
        br1=models.TextField()
        br2=models.TextField()
        br3=models.TextField()
        br4=models.TextField()
        br5=models.TextField()
