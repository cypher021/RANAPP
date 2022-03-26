# Generated by Django 4.0.2 on 2022-03-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('EventDescription', models.TextField()),
                ('Eventdate', models.DateField()),
                ('eventype', models.TextField(choices=[('Online', 'Online'), ('Physical', 'Physical')])),
            ],
        ),
        migrations.CreateModel(
            name='ProgramDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProgramName', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Objectives', models.TextField(help_text='Enter in bullet points')),
                ('Goals', models.TextField(help_text='Enter in bullet points')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('ProgramType', models.TextField(choices=[('Online', 'Online'), ('Physical', 'Physical')])),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=100)),
                ('ProjectDescription', models.TextField(blank=True, null=True)),
                ('Projectdate', models.DateField()),
                ('ProjectPOCname', models.CharField(max_length=100)),
                ('ProjectPOCnum', models.CharField(max_length=10)),
                ('Projectype', models.TextField(choices=[('Online', 'Online'), ('Physical', 'Physical')])),
                ('Projectlink', models.URLField()),
                ('ProjectTechnicalspecification', models.FileField(upload_to='', verbose_name='doc/')),
                ('ProjectWhitepapers', models.FileField(upload_to='', verbose_name='doc/whitepapers')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=100)),
                ('ServiceDescription', models.TextField()),
                ('Servicedate', models.DateField()),
                ('servicetype', models.TextField(choices=[('Online', 'Online'), ('Physical', 'Physical')])),
            ],
        ),
    ]