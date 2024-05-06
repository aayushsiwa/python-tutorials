# Generated by Django 5.0.4 on 2024-05-05 12:22

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tutorial_content_alter_tutorial_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 12, 22, 52, 131645, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
    ]