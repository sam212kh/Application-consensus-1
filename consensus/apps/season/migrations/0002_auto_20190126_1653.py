# Generated by Django 2.0.8 on 2019-01-26 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='school_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='school_id', to='school.School'),
        ),
    ]
