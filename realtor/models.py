from django.db import models

# Create your models here.
class Properties(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    address = models.CharField(max_length=250)
    price = models.IntegerField()
    size = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50)
    images = models.ImageField(upload_to='properties')
    location = models.CharField(max_length=100, blank=True, default="Nairobi")
    features = models.TextField(blank=True)
    # date_created = models.TimeField(b=True) 

    def __str__(self):
        return f'{self.title} created on {self.date_created}'


