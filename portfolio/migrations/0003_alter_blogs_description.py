# Generated by Django 5.0.4 on 2024-05-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
    ]
