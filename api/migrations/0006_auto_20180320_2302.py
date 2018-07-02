# Generated by Django 2.0.1 on 2018-03-20 22:02
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('api', '0005_auto_20180217_1542')]
    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(
                error_messages={
                    'unique': 'A user with that email address already exists.'
                },
                max_length=254,
                unique=True,
                verbose_name='email address',
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
