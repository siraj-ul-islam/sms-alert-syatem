# Generated by Django 4.1.4 on 2022-12-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_comment_dashboard', '0002_alter_unit_address_details_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit_contact_details',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]