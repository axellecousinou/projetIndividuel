# Generated by Django 2.1.15 on 2021-05-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]