# Generated by Django 4.1.4 on 2022-12-20 04:45

from django.db import migrations, models
import user_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('notification', models.CharField(blank=True, max_length=128, null=True)),
                ('is_seen', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('profile_image', models.ImageField(upload_to='profile/')),
                ('email_verified_at', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('remember_token', models.CharField(blank=True, default=True, max_length=128, null=True)),
                ('user_type', models.CharField(blank=True, choices=[(user_auth.models.UserTypesChoices['admin'], 'admin'), (user_auth.models.UserTypesChoices['user'], 'user')], default=True, max_length=128, null=True)),
                ('credit', models.CharField(blank=True, default=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
