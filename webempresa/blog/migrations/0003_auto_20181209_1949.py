# Generated by Django 2.1.3 on 2018-12-09 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181208_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre de categoría'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
