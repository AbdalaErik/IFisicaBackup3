# Generated by Django 4.2.7 on 2023-11-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_ocupacao_options_alter_pessoa_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='descricao',
            field=models.CharField(max_length=1000, verbose_name='Descrição'),
        ),
    ]