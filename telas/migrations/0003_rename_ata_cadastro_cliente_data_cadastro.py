# Generated by Django 3.2.7 on 2021-09-22 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telas', '0002_auto_20210922_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ata_cadastro',
            new_name='data_cadastro',
        ),
    ]