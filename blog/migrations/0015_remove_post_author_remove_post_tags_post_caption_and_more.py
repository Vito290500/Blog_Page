# Generated by Django 4.2.1 on 2023-06-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='e_mail_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]