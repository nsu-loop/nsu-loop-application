# Generated by Django 3.2.1 on 2021-05-05 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField(default='no bio...', max_length=300)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('major', models.CharField(blank=True, max_length=200, null=True)),
                ('cgpa', models.FloatField(blank=True, null=True)),
                ('grad_year', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='avatars/')),
                ('skills', models.JSONField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
