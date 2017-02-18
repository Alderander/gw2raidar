# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 16:30
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(re.compile('\\S+\\.\\d{4}', 32))])),
                ('api_key', models.CharField(blank=True, max_length=72, validators=[django.core.validators.RegexValidator(re.compile('[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{20}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$', 34))], verbose_name='API key')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('profession', models.PositiveSmallIntegerField(choices=[(1, 'Guardian'), (2, 'Warrior'), (3, 'Engineer'), (4, 'Ranger'), (5, 'Thief'), (6, 'Elementalist'), (7, 'Mesmer'), (8, 'Necromancer'), (9, 'Revenant')])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidar.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raidar.Area')),
                ('characters', models.ManyToManyField(to='raidar.Character')),
            ],
        ),
    ]