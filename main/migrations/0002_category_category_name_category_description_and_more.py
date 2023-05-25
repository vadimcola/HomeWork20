# Generated by Django 4.2.1 on 2023-05-25 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Наименование категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=True, max_length=255, verbose_name='Наименование продукта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]