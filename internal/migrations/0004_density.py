# Generated by Django 3.2.4 on 2021-07-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_streamgraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='density',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
