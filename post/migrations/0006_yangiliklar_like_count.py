# Generated by Django 4.0.3 on 2022-05-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_yangiliklar_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
