# Generated by Django 4.2 on 2024-03-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0005_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prediction_result',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
