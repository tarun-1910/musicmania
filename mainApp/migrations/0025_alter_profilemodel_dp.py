# Generated by Django 4.1.3 on 2022-12-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_alter_profilemodel_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='dp',
            field=models.ImageField(blank=True, default='kurtCobain.jpg', null=True, upload_to=''),
        ),
    ]