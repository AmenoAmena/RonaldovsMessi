# Generated by Django 4.2.7 on 2024-02-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RvM_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_m', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
