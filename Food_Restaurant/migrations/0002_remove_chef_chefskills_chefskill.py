# Generated by Django 5.1.6 on 2025-04-04 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='ChefSkills',
        ),
        migrations.CreateModel(
            name='ChefSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_percentage', models.PositiveIntegerField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='Food_Restaurant.chef')),
            ],
        ),
    ]
