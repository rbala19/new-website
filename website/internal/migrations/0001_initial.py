# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 02:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('semester_joined', models.CharField(blank=True, max_length=6, verbose_name=[django.core.validators.RegexValidator('(fa|sp)20[0-9][0-9]')])),
                ('status', models.CharField(choices=[('active', 'Active'), ('associate_first', 'First Semester Associate'), ('associate_second', 'Second Semester Associate'), ('alumni', 'Alumni')], max_length=16)),
                ('bio', models.TextField(blank=True)),
                ('attendance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('title', models.TextField(default='General Member')),
                ('cell_phone', models.CharField(blank=True, max_length=11)),
                ('facebook', models.CharField(blank=True, max_length=300)),
                ('instagram', models.CharField(blank=True, max_length=300)),
                ('snapchat', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('time', models.DateTimeField()),
                ('speaker_first_name', models.CharField(max_length=100)),
                ('speaker_last_name', models.CharField(max_length=100)),
                ('speaker_bio', models.TextField()),
                ('projected_attendance', models.IntegerField()),
                ('venue', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('facebook_link', models.CharField(max_length=300)),
                ('eventbrite_link', models.CharField(max_length=300)),
                ('elf_link', models.CharField(max_length=300)),
                ('elf_exemption_link', models.CharField(max_length=300)),
                ('fbcover_link', models.CharField(max_length=300)),
                ('websitephoto_link', models.CharField(max_length=300)),
                ('seal_link', models.CharField(max_length=300)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to=settings.AUTH_USER_MODEL)),
                ('point_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pp_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('friendly_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internal.Group')),
            ],
            bases=('internal.group',),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internal.Group')),
            ],
            bases=('internal.group',),
        ),
        migrations.CreateModel(
            name='SubCommittee',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internal.Group')),
            ],
            bases=('internal.group',),
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='subcommittee',
            name='members',
            field=models.ManyToManyField(related_name='subcommittees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcommittee',
            name='parent_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcommittees', to='internal.Committee'),
        ),
        migrations.AddField(
            model_name='subcommittee',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='division',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='division',
            name='members',
            field=models.ManyToManyField(related_name='divisions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='committee',
            name='members',
            field=models.ManyToManyField(related_name='committees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='committee',
            name='vp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
