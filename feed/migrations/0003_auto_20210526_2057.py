# Generated by Django 3.1.5 on 2021-05-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20210526_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
