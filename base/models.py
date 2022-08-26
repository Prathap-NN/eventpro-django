from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=191, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    event_start_date = models.DateField(blank=True, null=True)
    event_end_date = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=191, blank=True, null=True)
    campus = models.CharField(max_length=191, blank=True, null=True)
    tags = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    event_start_time = models.CharField(max_length=10, blank=True, null=True)
    event_end_time = models.CharField(max_length=10, blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_online_event = models.CharField(max_length=3, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    facebook = models.CharField(max_length=191, blank=True, null=True)
    youtube = models.CharField(max_length=191, blank=True, null=True)
    instagram = models.CharField(max_length=191, blank=True, null=True)
    twitter = models.CharField(max_length=191, blank=True, null=True)
    featured_img = models.ImageField(blank=True, null=True)
    attachment = models.CharField(max_length=200,blank=True,null=True)
    images = models.ImageField(upload_to='images',max_length=200,blank=True,null=True)
    # attachment = models.TextField(blank=True, null=True)
    # likes = models.ManyToManyField(blank=True, null=True)
    # view_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    external_link = models.TextField(blank=True, null=True)
    club_name = models.CharField(max_length=191, blank=True, null=True)
    button_name = models.CharField(max_length=20, blank=True, null=True)
    custom_text = models.CharField(max_length=100, blank=True, null=True)
    # event_price = models.IntegerField(blank=True, null=True)
    event_attendees = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    publish = models.CharField(max_length=20, blank=True, null=True)
    google_map = models.CharField(max_length=15, blank=True, null=True)



    def __str__(self):
          return self.name
    
    def num_likse(self):
         return self.likes.all().count()

class Meta:
        managed = False
        db_table = 'eventsdbb'
        ordering = ['-updated', '-created']

