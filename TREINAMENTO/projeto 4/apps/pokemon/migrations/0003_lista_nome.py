# Generated by Django 5.0.6 on 2024-07-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_rename_jogos_jogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='nome',
            field=models.CharField(default=0.01, max_length=50),
            preserve_default=False,
        ),
    ]