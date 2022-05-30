# Generated by Django 3.2.13 on 2022-05-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220520_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]