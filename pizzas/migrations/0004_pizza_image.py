# Generated by Django 3.2 on 2021-04-30 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
