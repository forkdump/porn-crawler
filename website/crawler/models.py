from django.db import models

# Create your models here.
class query(models.Model):
    keyword = models.TextField()
    class Meta:
        db_table = "query"

class videos(models.Model):
    title = models.TextField()
    url = models.TextField()
    logo = models.TextField()
    class Meta:
        db_table = "videos"

class videos_after_searched(models.Model):
    title = models.TextField()
    url = models.TextField()
    logo = models.TextField()
    class Meta:
        db_table = "videos_after_searched"