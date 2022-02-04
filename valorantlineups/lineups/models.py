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
    xPos = models.IntegerField()
    yPos = models.IntegerField()
    childPinAmount = models.IntegerField()

    # can use JSONField as a list -> https://stackoverflow.com/questions/40241014/django-jsonfield-contains-list-of-values
    childPinIds = models.JSONField()

    isAttacking = models.BooleanField()
    rating = models.FloatField()
    createdOn = models.DateTimeField(max_length=10)
    author = models.CharField(max_length=64)

class ChildLineup(models.Model):
    name = models.CharField(max_length=32)
    xPos = models.IntegerField()
    yPos = models.IntegerField()

class Map(models.Model):
    name = models.CharField(max_length=32)
    numLineups = models.IntegerField()
