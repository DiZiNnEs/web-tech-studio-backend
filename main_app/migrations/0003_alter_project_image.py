# Generated by Django 3.2.4 on 2021-06-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210612_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media/images/projects/%Y/%m/'),
        ),
    ]
