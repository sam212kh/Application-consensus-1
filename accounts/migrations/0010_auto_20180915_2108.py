# Generated by Django 2.1.1 on 2018-09-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180915_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='application_reviews_required',
            field=models.IntegerField(default=3, help_text='Reviews required for each application received'),
        ),
    ]
