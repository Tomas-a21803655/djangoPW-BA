# Generated by Django 3.2.3 on 2021-06-01 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0015_quizzaval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizzaval',
            old_name='monthsProject',
            new_name='diff',
        ),
    ]
