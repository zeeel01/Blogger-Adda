# Generated by Django 3.2.6 on 2021-10-06 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_userimage_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]