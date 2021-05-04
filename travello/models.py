from django.db import models

# Create your models here.


class Destination(models.Model):
    # commands for migrating this class in to database
    # python manage.py makemigrations
    # python manage.py sqlmigrate travello 0001
    # python manage.py migrate
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

