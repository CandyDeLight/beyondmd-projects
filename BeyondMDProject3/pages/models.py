"""
first: "python3 manage.py makemigrations" to generate the SQL commands
second: "python3 manage.py migrate" to run the SQL commands
"""

from django.db import models

# Create your models here.

class Reviews(models.Model):
    """
    Reviews is the table. the attributes are movie_titles, poster, rating, comment, and user_id
    it also has id or primary key but that is auto generated
    """
    movie_title = models.CharField(max_length=750)
    poster = models.CharField(max_length=1250, default="")
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    user_id = models.PositiveIntegerField(default="1")