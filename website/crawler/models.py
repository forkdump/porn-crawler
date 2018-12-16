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
        