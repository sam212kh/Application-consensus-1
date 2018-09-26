# Generated by Django 2.1.1 on 2018-09-07 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='application_text',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_school',
        ),
        migrations.AddField(
            model_name='school',
            name='max_batch_size',
            field=models.IntegerField(blank=True, help_text='Maximum students to enroll each year in a batch', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='batch_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_batches', to='accounts.School'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batch_students', to='accounts.Batch'),
        ),
    ]