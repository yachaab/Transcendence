# Generated by Django 5.0.7 on 2024-08-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gameInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('gamesPlayed', models.IntegerField(default=0)),
                ('codeToPlay', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('you', models.CharField(max_length=20)),
                ('oppenent', models.CharField(max_length=20)),
                ('winner', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='playerAndHisPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('pic', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='players',
        ),
    ]
