# Generated by Django 4.2.7 on 2023-12-18 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitedog', '0005_category_sitedog_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedog',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sitedog.category'),
        ),
    ]
