# Generated by Django 4.0.3 on 2022-05-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_alter_resulttype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttype',
            name='image',
            field=models.ImageField(upload_to='firstapp/static/firstapp/img/'),
        ),
    ]