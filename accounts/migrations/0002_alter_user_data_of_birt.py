# Generated by Django 4.1.1 on 2022-09-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_of_birt',
            field=models.DateField(null=True),
        ),
    ]