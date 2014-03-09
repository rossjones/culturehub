from django.db import models


class Place(models.Model):

    title = models.TextField()
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Restaurant(models.Model):

    name = models.TextField()
    address = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    hygiene_rating = models.IntegerField(null=True, blank=True)
    structural_rating = models.IntegerField(null=True, blank=True)
    management_rating = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name
