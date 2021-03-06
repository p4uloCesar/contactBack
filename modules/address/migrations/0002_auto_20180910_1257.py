# Generated by Django 2.1 on 2018-09-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='district',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, db_column='city', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, db_column='country', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, db_column='number', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, db_column='state', max_length=500, null=True),
        ),
    ]
