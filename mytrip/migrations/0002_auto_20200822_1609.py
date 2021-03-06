# Generated by Django 3.1 on 2020-08-22 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytrip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='city',
        ),
        migrations.AddField(
            model_name='trip',
            name='destination_city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='mytrip.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='source_city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='source_city', to='mytrip.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
