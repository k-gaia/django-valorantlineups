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
    ASTRA = 'AS', 'Astra'
    BREACH = 'BRE', 'Breach'
    BRIMSTONE = 'BRI', 'Brimstone'
    CHAMBER = 'CH', 'Chamber'
    CYPHER = 'CY', 'Cypher'
    JETT = 'JE', 'Jett'
    KILLJOY = 'KI', 'Killjoy'
    KAYO = 'KA', 'KAY/O'
    NEON = 'NE', 'Neon'
    OMEN = 'OM', 'Omen'
    PHOENIX = 'PH', 'Phoenix'
    RAZE = 'RA', 'Raze'
    REYNA = 'RE', 'Reyna'
    SAGE = 'SA', 'Sage'
    SKYE = 'SK', 'Skye'
    SOVA = 'SO', 'Sova'
    VIPER = 'VI', 'Viper'
    YORU = 'YO', 'Yoru'

class Maps(models.TextChoices):
    ASCENT = 'AS', 'Ascent'
    BIND = 'BI', 'Bind'
    BREEZE = 'BR', 'Breeze'
    FRACTURE = 'FR', 'Fracture'
    HAVEN = 'HA', 'Haven'
    ICEBOX = 'IC', 'Icebox'
    SPLIT = 'SP', 'Split'


class Lineup(models.Model):
    name = models.CharField(max_length=32)
    map = models.CharField(max_length=16, choices=Maps.choices)
    character = models.CharField(max_length=64, choices=Agents.choices)
    ability = models.CharField(max_length=64)
    xPos = models.IntegerField()
    yPos = models.IntegerField()
    childPinAmount = models.IntegerField()

    # can use JSONField as a list -> https://stackoverflow.com/questions/40241014/django-jsonfield-contains-list-of-values
    childPinIds = models.JSONField()

    isAttacking = models.BooleanField()
    rating = models.FloatField()
    createdOn = models.DateTimeField(max_length=10)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.map + " - " + self.name + " - " + self.character + " - " + self.ability  + " - " + str(self.rating)

class ChildLineup(models.Model):
    name = models.CharField(max_length=32)
    content = models.URLField()
    xPos = models.IntegerField()
    yPos = models.IntegerField()

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + self.content + " - " + str(self.xPos) + " - " + str(self.yPos)

class Map(models.Model):
    name = models.CharField(max_length=32)
    numLineups = models.IntegerField()
