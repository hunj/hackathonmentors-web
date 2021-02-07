# Generated by Django 3.0.7 on 2020-06-25 06:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('skills', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=models.SET(1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mentors',
            },
        ),
    ]