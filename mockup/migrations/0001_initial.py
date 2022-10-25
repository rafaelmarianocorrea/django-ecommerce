# Generated by Django 3.2 on 2022-10-25 14:13

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
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('shirtStyle', models.CharField(max_length=255)),
                ('shirtPlacement', models.CharField(max_length=255)),
                ('shirtColor', models.CharField(max_length=255)),
                ('document', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('artWidth', models.IntegerField(blank=True, null=True)),
                ('artPosTop', models.IntegerField(blank=True, null=True)),
                ('artPosLeft', models.IntegerField(blank=True, null=True)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('textFont', models.CharField(blank=True, max_length=255, null=True)),
                ('textSize', models.IntegerField(blank=True, null=True)),
                ('textColor', models.CharField(blank=True, max_length=50, null=True)),
                ('textPosTop', models.IntegerField(blank=True, null=True)),
                ('textPosLeft', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
