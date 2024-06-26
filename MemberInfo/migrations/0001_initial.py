# Generated by Django 5.0.4 on 2024-04-15 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('goal', models.CharField(choices=[('Lose weight', 'Lose weight'), ('Maintain weight', 'Maintain weight'), ('Gain weight', 'Gain weight'), ('Gain muscle', 'Gain muscle')], max_length=255)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255)),
                ('age', models.IntegerField(default=18)),
                ('height', models.IntegerField(default=150)),
                ('weight', models.FloatField(default=50)),
                ('weight_goal', models.FloatField(default=50)),
                ('activity_level', models.CharField(choices=[('Sedentary', 'Sedentary'), ('Lightly active', 'Lightly active'), ('Moderately active', 'Moderately active'), ('Very  active', 'Very active'), ('Extra active', 'Extra active')], max_length=255)),
                ('memberid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
