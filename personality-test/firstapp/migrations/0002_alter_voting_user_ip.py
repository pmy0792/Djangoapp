# Generated by Django 4.0.3 on 2022-05-17 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='user_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='firstapp.user'),
        ),
    ]
