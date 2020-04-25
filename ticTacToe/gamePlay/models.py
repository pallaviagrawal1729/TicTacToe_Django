from django.db import models
from django.contrib.auth.models import User

'''
Django comes with default User class, Django will add columns based on
the other side of relation i.e. via ForeignKey reference
'''


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)
    # auto_now helps update time-stamp every time
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)


class Move(models.Model):
    # Django adds primary key
    # x co-ord of where the move was made
    x = models.IntegerField()
    # y co-ord of where the move was made
    y = models.IntegerField()
    # by default all columns are specified as 'Not Null' but CharField allows you to leave empty
    comment = models.CharField(max_length=300, blank=True)
    # boolean value is used to decide which player made the move
    by_first_player = models.BooleanField()
    # a many-to-one relation i.e. for a game we will have multiple moves
    # on counter part Django will create a move set to store moves
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

