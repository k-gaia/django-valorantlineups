from sys import maxsize
from django.db import models

# Choice Variables
con = "CONTROLLER"
duel = "DUELIST"
init = "INITIATOR"
sent = "SENTINEL"

AGENTCLASS_CHOICES = (

    (con, "controller"),
    (duel, "duelist"),
    (init, "initiator"),
    (sent, "sentinel")

)

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=64)
    agentClass = models.CharField(max_length=16, choices=AGENTCLASS_CHOICES, default='CONTROLLER')
    cAbility = models.CharField(max_length=30)
    qAbility = models.CharField(max_length=30)
    eAbility = models.CharField(max_length=30)
    xAbility = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + " - " + self.agentClass

class Lineup(models.Model):
    name = models.CharField(max_length=32)
    xPos = models.IntegerField(max_length=255)
    yPos = models.IntegerField(max_length=255)
    childPinAmount = models.IntegerField(max_length=255)

    # can use JSONField as a list -> https://stackoverflow.com/questions/40241014/django-jsonfield-contains-list-of-values
    childPinIds = models.JSONField(maxsize=255)

    isAttacking = models.BooleanField()
    rating = models.FloatField(max_length=255)
    createdOn = models.DateTimeField(max_length=10)
    author = models.CharField(max_length=64)

class ChildLineup(models.Model):
    name = models.CharField(max_length=32)
    xPos = models.IntegerField(max_length=255)
    yPos = models.IntegerField(max_length=255)

class Map(models.Model):
    name = models.CharField(max_length=32)
    numLineups = xPos = models.IntegerField(max_length=255)
