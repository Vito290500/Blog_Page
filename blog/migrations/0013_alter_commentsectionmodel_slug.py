# Generated by Django 4.2.1 on 2023-06-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_commentsectionmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsectionmodel',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
