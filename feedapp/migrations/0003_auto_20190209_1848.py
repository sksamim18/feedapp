# Generated by Django 2.1.5 on 2019-02-09 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedapp', '0002_auto_20190208_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['user_username'], 'verbose_name': 'Posted comment', 'verbose_name_plural': 'Posted comment list'},
        ),
    ]
