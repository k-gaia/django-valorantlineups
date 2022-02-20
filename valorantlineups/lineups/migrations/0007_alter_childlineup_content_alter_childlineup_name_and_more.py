# Generated by Django 4.0.1 on 2022-02-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineups', '0006_childlineup_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childlineup',
            name='content',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='childlineup',
            name='name',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='childlineup',
            name='xPos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='childlineup',
            name='yPos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='ability',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='author',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='character',
            field=models.CharField(blank=True, choices=[('AS', 'Astra'), ('BRE', 'Breach'), ('BRI', 'Brimstone'), ('CH', 'Chamber'), ('CY', 'Cypher'), ('JE', 'Jett'), ('KI', 'Killjoy'), ('KA', 'KAY/O'), ('NE', 'Neon'), ('OM', 'Omen'), ('PH', 'Phoenix'), ('RA', 'Raze'), ('RE', 'Reyna'), ('SA', 'Sage'), ('SK', 'Skye'), ('SO', 'Sova'), ('VI', 'Viper'), ('YO', 'Yoru')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='childPinAmount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='childPinIds',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='createdOn',
            field=models.DateTimeField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='isAttacking',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='map',
            field=models.CharField(blank=True, choices=[('AS', 'Ascent'), ('BI', 'Bind'), ('BR', 'Breeze'), ('FR', 'Fracture'), ('HA', 'Haven'), ('IC', 'Icebox'), ('SP', 'Split')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='xPos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lineup',
            name='yPos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]