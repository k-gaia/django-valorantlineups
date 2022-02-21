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

class Agents(models.TextChoices):
    ASTRA = 'Astra'
    BREACH = 'Breach'
    BRIMSTONE = 'Brimstone'
    CHAMBER = 'Chamber'
    CYPHER = 'Cypher'
    JETT = 'Jett'
    KILLJOY = 'Killjoy'
    KAYO = 'KAY/O'
    NEON = 'Neon'
    OMEN = 'Omen'
    PHOENIX = 'Phoenix'
    RAZE = 'Raze'
    REYNA = 'Reyna'
    SAGE = 'Sage'
    SKYE = 'Skye'
    SOVA = 'Sova'
    VIPER = 'Viper'
    YORU = 'Yoru'

class Maps(models.TextChoices):
    ASCENT = 'Ascent'
    BIND = 'Bind'
    BREEZE = 'Breeze'
    FRACTURE = 'Fracture'
    HAVEN = 'Haven'
    ICEBOX = 'Icebox'
    SPLIT = 'Split'


class Lineup(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    map = models.CharField(max_length=16, choices=Maps.choices, null=True, blank=True)
    character = models.CharField(max_length=64, choices=Agents.choices, null=True, blank=True)
    ability = models.CharField(max_length=64, null=True, blank=True)
    xPos = models.IntegerField(null=True, blank=True)
    yPos = models.IntegerField(null=True, blank=True)
    childPinAmount = models.IntegerField(null=True, blank=True)

    # can use JSONField as a list -> https://stackoverflow.com/questions/40241014/django-jsonfield-contains-list-of-values
    childPinIds = models.JSONField(null=True, blank=True)

    isAttacking = models.BooleanField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    createdOn = models.DateTimeField(max_length=10, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)

class ChildLineup(models.Model):
    name = models.CharField(max_length=32, blank=True)
    content = models.URLField(blank=True)
    xPos = models.IntegerField(blank=True)
    yPos = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + self.content + " - " + str(self.xPos) + " - " + str(self.yPos)

class Map(models.Model):
    name = models.CharField(max_length=32)
    numLineups = models.IntegerField()
