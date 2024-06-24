# Generated by Django 5.0.6 on 2024-06-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pagina1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('foto', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='pagina2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('arquivo', models.FileField(upload_to='pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='pagina3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Ferminino')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PGinicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('data', models.DateField()),
            ],
        ),
    ]
