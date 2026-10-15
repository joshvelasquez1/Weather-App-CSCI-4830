from django.db import models

class SearchHistory(models.Model):
    location = models.CharField(max_length=100)
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    condition = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)
