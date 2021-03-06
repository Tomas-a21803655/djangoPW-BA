# Generated by Django 3.2.3 on 2021-05-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0011_remove_comment_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Networking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('satisfaction', models.IntegerField(default='5')),
                ('destination', models.CharField(max_length=200)),
                ('visitDate', models.DateField(blank=True, null=True)),
                ('groupSize', models.IntegerField(blank=True, null=True)),
                ('useAgain', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
