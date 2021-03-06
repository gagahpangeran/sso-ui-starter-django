# Generated by Django 2.1.5 on 2019-01-17 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_code', models.CharField(blank=True, max_length=11, verbose_name='kode organisasi')),
                ('role', models.CharField(blank=True, max_length=128, verbose_name='peran pengguna')),
                ('npm', models.CharField(blank=True, max_length=10, verbose_name='Nomor Pokok Mahasiswa')),
                ('faculty', models.CharField(blank=True, max_length=128, verbose_name='fakultas')),
                ('study_program', models.CharField(blank=True, max_length=128, verbose_name='program studi')),
                ('educational_program', models.CharField(blank=True, max_length=128, verbose_name='program pendidikan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profil',
                'verbose_name_plural': 'profil',
            },
        ),
    ]
