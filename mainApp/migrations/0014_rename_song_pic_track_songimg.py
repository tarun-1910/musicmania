# Generated by Django 4.1.3 on 2022-11-11 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_remove_profilemodel_profile_pic_profilemodel_dp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='song_pic',
            new_name='songImg',
        ),
    ]
