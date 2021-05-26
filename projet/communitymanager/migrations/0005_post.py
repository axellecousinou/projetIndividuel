# Generated by Django 2.1.15 on 2021-05-18 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communitymanager', '0004_auto_20210518_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date_creation', models.DateTimeField()),
                ('evenementiel', models.BooleanField()),
                ('date_evenement', models.DateTimeField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('communaute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communitymanager.Communaute')),
                ('priorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communitymanager.Priorite')),
            ],
        ),
    ]