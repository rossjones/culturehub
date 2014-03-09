from django.db import models

from culturehub.places.models import Place

class Event(models.Model):

    title = models.TextField()
    description = models.TextField()
    place = models.ForeignKey(Place)
    #organiser
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    image_thumb = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
