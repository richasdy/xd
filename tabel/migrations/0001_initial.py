# Generated by Django 3.2.4 on 2021-07-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=30)),
                ('pesan', models.TextField()),
            ],
        ),
    ]
