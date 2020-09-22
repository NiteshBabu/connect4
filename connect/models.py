from django.db import models

# Create your models here.

class Game (models.Model):
  token = models.TextField()
  moves = models.TextField()
  winner = models.CharField(max_length=2)

  def __str__(self):
    return f"{self.token} | Winner -> {self.winner}"
