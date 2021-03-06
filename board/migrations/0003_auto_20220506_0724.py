# Generated by Django 3.2.13 on 2022-05-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_bintime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bintime',
            name='cpu_per',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='bintime',
            name='max_size',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bintime',
            name='mpage_fault',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bintime',
            name='page_fault',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
