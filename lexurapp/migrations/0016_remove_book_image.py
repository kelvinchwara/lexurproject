# Generated by Django 5.1.3 on 2024-12-04 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0015_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
