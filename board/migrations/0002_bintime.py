# Generated by Django 3.2.13 on 2022-05-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bintime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elf_name', models.CharField(max_length=200)),
                ('run_time', models.DateTimeField(auto_now_add=True)),
                ('user_time', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sys_time', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cpu_per', models.CharField(max_length=5)),
                ('elapse_time', models.DecimalField(decimal_places=3, max_digits=6)),
                ('max_size', models.CharField(max_length=8)),
                ('page_fault', models.CharField(max_length=6)),
                ('mpage_fault', models.CharField(max_length=8)),
            ],
        ),
    ]