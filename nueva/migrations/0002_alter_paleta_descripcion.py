# Generated by Django 4.2.5 on 2023-10-11 00:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nueva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paleta',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
