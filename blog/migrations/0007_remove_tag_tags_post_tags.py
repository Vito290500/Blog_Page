# Generated by Django 4.2.1 on 2023-06-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_tag_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]