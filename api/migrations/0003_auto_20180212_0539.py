# Generated by Django 2.0.1 on 2018-02-12 04:39
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('api', '0002_auto_20180212_0530')]
    operations = [
        migrations.RenameField(
            model_name='service', old_name='categories', new_name='category'
        )
    ]