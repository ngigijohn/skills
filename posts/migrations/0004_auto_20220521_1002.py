# Generated by Django 3.2.13 on 2022-05-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220520_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='industry',
        ),
        migrations.AddField(
            model_name='post',
            name='specialization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
