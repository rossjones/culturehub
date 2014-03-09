from django.db import models


class Category(models.Model):

    title = models.TextField()
    interesting = models.BooleanField()

    def __unicode__(self):
        return self.title