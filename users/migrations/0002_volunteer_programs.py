# Generated by Django 3.0.1 on 2020-07-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer_Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(help_text='title of the programs', max_length=200)),
                ('Description', models.CharField(help_text='description of the program', max_length=400)),
            ],
        ),
    ]
