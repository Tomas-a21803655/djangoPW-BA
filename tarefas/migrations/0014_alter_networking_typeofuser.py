# Generated by Django 3.2.3 on 2021-05-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0013_networking_typeofuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networking',
            name='typeOfUser',
            field=models.BooleanField(choices=[(True, 'Guide'), (False, 'Tourist')], default=False),
        ),
    ]
