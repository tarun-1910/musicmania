# Generated by Django 4.1.3 on 2022-12-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_alter_profilemodel_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='dp',
            field=models.ImageField(blank=True, default='static/assets/img/kurtCobain.jpg', null=True, upload_to=''),
        ),
    ]
