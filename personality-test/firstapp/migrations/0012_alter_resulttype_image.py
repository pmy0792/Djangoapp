# Generated by Django 4.0.3 on 2022-05-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttype',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
