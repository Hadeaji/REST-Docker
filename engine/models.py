from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Engine_1(models.Model):
    engine_name = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    game_name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.game_name