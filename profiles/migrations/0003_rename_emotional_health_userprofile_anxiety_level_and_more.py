# Generated by Django 4.2.7 on 2023-11-23 17:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_emotional_health_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='emotional_health',
            new_name='anxiety_level',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='social_health',
            new_name='depression_level',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mental_health_awareness',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='relationship_health',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
