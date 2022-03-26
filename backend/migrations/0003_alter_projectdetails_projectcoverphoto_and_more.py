# Generated by Django 4.0.2 on 2022-03-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_projectdetails_projectcoverphoto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='ProjectCoverphoto',
            field=models.ImageField(default='defaultcover.jpg', help_text='The size must be --- and the resoultion is ---', upload_to='images/coverphoto/ProjectDetails/'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='ProjectTechnicalspecification',
            field=models.FileField(blank=True, help_text='The file must be in pdf', upload_to='doc/', verbose_name='Technical specification'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='ProjectWhitepapers',
            field=models.FileField(blank=True, help_text='The file must be in pdf', upload_to='doc/whitepapers', verbose_name='White papers'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='Projectdate',
            field=models.DateField(blank=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='Projectlink',
            field=models.URLField(blank=True, help_text='url link'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='Projectpicture',
            field=models.ImageField(default='default.jpg', help_text='The size must be --- and the resoultion is ---', upload_to='images/Photo/ProjectDetails/'),
        ),
    ]