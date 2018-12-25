from django.db import models

# Create your models here.
class Avgle(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "avgle"

class Youporn(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "youporn"

class Pornhub(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "pornhub"

class Tube85(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "tube85"

class Redtube(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "redtube"

class Popjav(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "popjav"

class Thisav(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "thisav"

class Xvideos(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "xvideos"

class Query(models.Model):
    keyword = models.TextField()
    class Meta:
        db_table = "query"

class AvgleQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "avgle_query"

class YoupornQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "youporn_query"

class PornhubQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "pornhub_query"

class Tube85Query(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "tube85_query"

class RedtubeQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "redtube_query"

class PopjavQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "popjav_query"

class ThisavQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "thisav_query"

class XvideosQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "xvideos_query"
        