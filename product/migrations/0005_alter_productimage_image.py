# Generated by Django 4.1.2 on 2022-10-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]