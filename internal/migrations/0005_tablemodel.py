# Generated by Django 3.2.4 on 2021-07-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0004_density'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=16)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]