# Generated by Django 3.2.6 on 2022-10-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_comment_commentblog_new_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentblog',
            name='asked_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]