# Generated by Django 4.2.7 on 2023-11-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_topico_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='descricao',
            field=models.CharField(max_length=2000, verbose_name='Descrição'),
        ),
    ]
