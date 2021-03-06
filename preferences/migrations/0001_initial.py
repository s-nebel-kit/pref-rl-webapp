# Generated by Django 3.2.8 on 2021-10-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('updated_timestamp', models.DateTimeField(auto_now=True, db_index=True, verbose_name='last updated at')),
                ('video_url_left', models.TextField(db_index=True, verbose_name='video url left')),
                ('video_url_right', models.TextField(db_index=True, verbose_name='video url right')),
                ('shown_to_human_timestamp', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='shown to human at')),
                ('response_timestamp', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='response given at')),
                ('label', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='preference label')),
            ],
        ),
    ]
