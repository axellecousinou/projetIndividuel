# Generated by Django 2.1.15 on 2021-05-18 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0003_post_titre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='post',
            name='communaute',
        ),
        migrations.RemoveField(
            model_name='post',
            name='priorite',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
