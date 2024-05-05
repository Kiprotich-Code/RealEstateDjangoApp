from django.db import models

# Create your models here.
class Properties(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    address = models.CharField(max_length=250)
    price = models.IntegerField()
    size = models.CharField(max_length=50, blank=True)
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.IntegerField(blank=True)
    amentities = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50)
    year_built = models.IntegerField()
    images = models.ImageField(upload_to='images/properties')
    location = models.CharField(max_length=100)
    features = models.TextField(blank=True)

    def __str__(self):
        return self.title.split()[0]

