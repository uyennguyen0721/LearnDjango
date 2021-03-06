# Generated by Django 3.2.5 on 2021-07-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210717_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]
