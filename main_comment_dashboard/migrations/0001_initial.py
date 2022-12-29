# Generated by Django 4.1.4 on 2022-12-20 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='unit_address_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=True)),
                ('unit_address', models.CharField(blank=True, max_length=225, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'unit_address_details',
            },
        ),
        migrations.CreateModel(
            name='unit_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=True)),
                ('unit_name', models.CharField(blank=True, default=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'unit_details',
            },
        ),
        migrations.CreateModel(
            name='unit_contact_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=True)),
                ('rank_message_sender', models.CharField(blank=True, max_length=60)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('unit_address_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_comment_dashboard.unit_address_details')),
                ('unit_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_comment_dashboard.unit_details')),
            ],
            options={
                'db_table': 'unit_contact_details',
            },
        ),
        migrations.CreateModel(
            name='unit_comment_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=True)),
                ('problem', models.CharField(blank=True, max_length=225, null=True)),
                ('vehicle_no', models.CharField(blank=True, max_length=225)),
                ('driver_name', models.CharField(blank=True, max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('unit_address_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_comment_dashboard.unit_address_details')),
            ],
            options={
                'db_table': 'unit_comment_details',
            },
        ),
        migrations.AddField(
            model_name='unit_address_details',
            name='unit_details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_comment_dashboard.unit_details'),
        ),
    ]
