# Generated by Django 5.1.3 on 2024-12-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexurapp', '0014_book_delete_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]
