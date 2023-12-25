# Generated by Django 4.2.7 on 2023-12-24 12:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitedog', '0007_tagpost_alter_sitedog_cat_sitedog_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='sitedog',
            options={'ordering': ['-time_create'], 'verbose_name': 'Породы собак', 'verbose_name_plural': 'Породы собак'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='sitedog.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='sitedog.tagpost', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='sitedog',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]