# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 17:01
from __future__ import unicode_literals

import base.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'jobs', '0001_initial'), (b'jobs', '0002_execution_time_limit'), (b'jobs', '0003_submitting_status_option'), (b'jobs', '0004_submission_output'), (b'jobs', '0005_upload_unique_random_filename')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participants', '0007_add_team_participant'),
        ('challenges', '0007_rename_test_environment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('submitted', 'submitted'), ('running', 'running'), ('failed', 'failed'), ('cancelled', 'cancelled'), ('finished', 'finished'), ('submitting', 'submitting')], max_length=30)),
                ('is_public', models.BooleanField(default=False)),
                ('submission_number', models.PositiveIntegerField(default=0)),
                ('download_count', models.IntegerField(default=0)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('when_made_public', models.DateTimeField(blank=True, null=True)),
                ('input_file', models.FileField(upload_to=base.utils.RandomFileName('submission_files/submission'))),
                ('stdout_file', models.FileField(blank=True, null=True, upload_to=base.utils.RandomFileName('submission_files/submission'))),
                ('stderr_file', models.FileField(blank=True, null=True, upload_to=base.utils.RandomFileName('submission_files/submission'))),
                ('challenge_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='challenges.ChallengePhase')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participant_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='participants.ParticipantTeam')),
                ('execution_time_limit', models.PositiveIntegerField(default=300)),
                ('output', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'submission',
            },
        ),
    ]
