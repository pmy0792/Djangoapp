# Generated by Django 4.0.3 on 2022-05-17 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_voting_user_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_ip',
            field=models.CharField(default='0.0.0.0', max_length=24, unique=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='user_ip',
            field=models.ForeignKey(default='0.0.0.0', on_delete=django.db.models.deletion.DO_NOTHING, to='firstapp.user'),
        ),
    ]
