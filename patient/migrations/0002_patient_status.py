# Generated by Django 5.0.4 on 2024-05-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], default='pending', max_length=10),
        ),
    ]
