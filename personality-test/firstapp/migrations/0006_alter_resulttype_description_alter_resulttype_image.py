# Generated by Django 4.0.3 on 2022-05-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_resulttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttype',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resulttype',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]