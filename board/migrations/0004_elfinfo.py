# Generated by Django 3.2.13 on 2022-05-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20220506_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elfinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elf_name', models.CharField(max_length=200)),
                ('text_length', models.DecimalField(decimal_places=0, max_digits=12)),
                ('data_length', models.DecimalField(decimal_places=0, max_digits=12)),
                ('bss_length', models.DecimalField(decimal_places=0, max_digits=12)),
                ('dec_length', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
        ),
    ]
