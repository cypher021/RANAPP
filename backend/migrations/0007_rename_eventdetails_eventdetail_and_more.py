# Generated by Django 4.0.2 on 2022-03-28 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_membership_socialsite1_membership_socialsite2_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventDetails',
            new_name='EventDetail',
        ),
        migrations.RenameModel(
            old_name='ProgramDetails',
            new_name='ProgramDetail',
        ),
        migrations.RenameModel(
            old_name='ProjectDetails',
            new_name='ProjectDetail',
        ),
        migrations.RenameModel(
            old_name='ServiceDetails',
            new_name='ServiceDetail',
        ),
        migrations.RenameModel(
            old_name='TenureDetails',
            new_name='TenureDetail',
        ),
    ]
