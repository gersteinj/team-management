# Generated by Django 2.0.4 on 2018-08-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20180806_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uid',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
