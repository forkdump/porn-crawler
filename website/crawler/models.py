from django.db import models

# Create your models here.
class Avgle(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Avgle"

class Youporn(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Youporn"

class Pornhub(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Pornhub"

class Tube85(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Tube85"

class Redtube(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Redtube"

class Popjav(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Popjav"

class Thisav(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Thisav"

class Xvideos(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Xvideos"

class Query(models.Model):
    keyword = models.TextField()
    class Meta:
        db_table = "Query"

class AvgleQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "AvgleQuery"

class YoupornQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "YoupornQuery"

class PornhubQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "PornhubQuery"

class Tube85Query(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "Tube85Query"

class RedtubeQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "RedtubeQuery"

class PopjavQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "PopjavQuery"

class ThisavQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "ThisavQuery"

class XvideosQuery(models.Model):
    title = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "XvideosQuery"
        