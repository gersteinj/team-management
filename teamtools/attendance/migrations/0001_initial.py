# Generated by Django 2.0.4 on 2018-08-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=255)),
                ('middle', models.CharField(blank=True, max_length=255, null=True)),
                ('last', models.CharField(max_length=255)),
                ('preferred', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
