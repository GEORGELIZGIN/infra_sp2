# Generated by Django 2.2.6 on 2021-07-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0002_auto_20210723_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='3274', max_length=128, verbose_name='confirmation_code'),
        ),
    ]
