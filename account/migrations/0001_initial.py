# Generated by Django 4.2.11 on 2024-03-07 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ammo',
            fields=[
                ('ammo_id', models.AutoField(primary_key=True, serialize=False)),
                ('ammo_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Smodel',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Suser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('permission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UAVS',
            fields=[
                ('serial', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('ammo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ammo')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.brands')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.smodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('rent_no', models.AutoField(primary_key=True, serialize=False)),
                ('rent_date_start', models.DateTimeField()),
                ('rent_date_end', models.DateTimeField()),
                ('rented_uav_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.uavs')),
                ('who_rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.suser')),
            ],
        ),
    ]
