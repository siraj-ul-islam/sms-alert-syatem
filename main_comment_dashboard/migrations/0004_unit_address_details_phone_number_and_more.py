# Generated by Django 4.1.4 on 2022-12-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_comment_dashboard', '0003_unit_contact_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit_address_details',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='unit_address_details',
            name='rank_message_sender',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='unit_address_details',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
