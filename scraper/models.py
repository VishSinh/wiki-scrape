from django.db import models

class WebScrape(models.Model):
    url = models.URLField( max_length=300)
    title = models.CharField(max_length=250)
    info = models.JSONField(null=True)
    timestamp = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.title
