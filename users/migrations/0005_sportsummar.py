# Generated by Django 3.0.1 on 2020-07-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='sportSummar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlings', models.CharField(help_text='sport summar headlings ', max_length=200)),
                ('body', models.CharField(help_text='sport summary body ', max_length=200)),
                ('HImage', models.ImageField(upload_to='sportimages')),
                ('Date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]