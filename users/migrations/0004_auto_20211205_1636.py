# Generated by Django 3.2.8 on 2021-12-05 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211205_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='scial_linkedin',
            new_name='social_linkedin',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='scial_twitter',
            new_name='social_twitter',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='scial_website',
            new_name='social_website',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='scial_youtube',
            new_name='social_youtube',
        ),
    ]
