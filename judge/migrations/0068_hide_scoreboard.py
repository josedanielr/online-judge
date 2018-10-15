# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0067_contest_access_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='hide_scoreboard',
            field=models.BooleanField(default=False, help_text='Whether the scoreboard should remain hidden for the duration of the contest.', verbose_name='hide scoreboard'),
        ),
        migrations.AlterField(
            model_name='problemtranslation',
            name='language',
            field=models.CharField(choices=[(b'de', 'German'), (b'en', 'English'), (b'es', 'Spanish'), (b'fr', 'French'), (b'hr', 'Croatian'), (b'ko', 'Korean'), (b'ro', 'Romanian'), (b'ru', 'Russian'), (b'sr-latn', 'Serbian (Latin)'), (b'vi', 'Vietnamese'), (b'zh-hans', 'Simplified Chinese')], max_length=7, verbose_name='language'),
        ),
    ]
