# Generated by Django 4.1.1 on 2022-09-15 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivername', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('bus_no', models.IntegerField()),
            ],
        ),
    ]