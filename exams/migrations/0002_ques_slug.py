# Generated by Django 2.1.2 on 2019-02-13 03:16

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ques',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title'),
        ),
    ]
