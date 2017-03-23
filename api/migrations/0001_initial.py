# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelname', models.CharField(max_length=30)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.College')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=20)),
                ('studentrollno', models.CharField(max_length=20)),
                ('studentbldgp', models.CharField(choices=[('1', 'O+ve'), ('2', 'AB+'), ('3', 'B')], max_length=3)),
                ('studentroomno', models.CharField(max_length=3)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.College')),
                ('hostelname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hostel')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.State')),
            ],
        ),
        migrations.AddField(
            model_name='hostel',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.State'),
        ),
        migrations.AddField(
            model_name='college',
            name='statename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.State'),
        ),
    ]