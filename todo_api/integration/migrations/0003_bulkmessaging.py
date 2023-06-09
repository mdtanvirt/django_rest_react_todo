# Generated by Django 4.1.7 on 2023-03-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0002_mailintegration_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkMessaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('profileName', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('selected', models.BooleanField(default=True)),
            ],
        ),
    ]
