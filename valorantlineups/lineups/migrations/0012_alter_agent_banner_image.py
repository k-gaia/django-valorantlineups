# Generated by Django 4.0.1 on 2022-04-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineups', '0011_agent_cability_agent_eability_agent_qability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='banner_image',
            field=models.FileField(upload_to='static/img/champBanners/'),
        ),
    ]
