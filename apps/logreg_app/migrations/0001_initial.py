# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-18 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=12)),
                ('confirm_password', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users_liked', models.ManyToManyField(related_name='users_liked', to='logreg_app.User')),
                ('wisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_this_wish', to='logreg_app.User')),
                ('wishes_granted', models.ManyToManyField(related_name='users_granted', to='logreg_app.User')),
            ],
        ),
    ]
