# Generated by Django 3.0.5 on 2020-05-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ploadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
