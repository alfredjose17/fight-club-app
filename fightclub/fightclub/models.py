from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=45, null=False, unique=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    password = models.CharField(max_length=225, null=True)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    player1_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_index=True, related_name='player1_matches', blank=True)
    player2_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_index=True, related_name='player2_matches', blank=True)
    match_date = models.DateField(null=True, blank=True)
    winner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='winner_matches', blank=True)

# class Registration(models.Model):
#     registration_id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, db_index=True)
#     match_id = models.ForeignKey('Match', on_delete=models.SET_NULL, null=True, db_index=True)
#     registration_date = models.DateField(null=True)
