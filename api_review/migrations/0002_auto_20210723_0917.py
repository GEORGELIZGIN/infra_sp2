# Generated by Django 2.2.6 on 2021-07-23 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]