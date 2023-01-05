from django.db import models

# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=200)
    biography=models.TextField()

    def __str__(self):
        return self.name



class Song(models.Model):
    title= models.TextField()
    artist= models.ManyToManyField(Artist, related_name='song')
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)

    def artist_names(self):
        return ', '.join([a.name for a in self.artist.all()])
    artist_names.short_description = "Artist Names"

    def __str__(self):
        return self.title

