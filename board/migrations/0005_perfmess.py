# Generated by Django 3.2.13 on 2022-05-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_elfinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfmess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elf_name', models.CharField(max_length=200)),
                ('params', models.CharField(max_length=200)),
                ('run_time', models.DateTimeField(auto_now_add=True)),
                ('cpu_utilize', models.DecimalField(decimal_places=3, max_digits=4)),
                ('instructions', models.DecimalField(decimal_places=0, max_digits=12)),
                ('branches', models.DecimalField(decimal_places=0, max_digits=12)),
                ('branches_misses', models.DecimalField(decimal_places=0, max_digits=12)),
                ('l1_dcache', models.DecimalField(decimal_places=0, max_digits=12)),
                ('l1_dcache_misses', models.DecimalField(decimal_places=0, max_digits=12)),
                ('llc_cache', models.DecimalField(decimal_places=0, max_digits=12)),
                ('llc_cache_misses', models.DecimalField(decimal_places=0, max_digits=12)),
                ('l1_icache', models.DecimalField(decimal_places=0, max_digits=12)),
                ('l1_icache_misses', models.DecimalField(decimal_places=0, max_digits=12)),
                ('dtlb_cache', models.DecimalField(decimal_places=0, max_digits=12)),
                ('dtlb_cache_misses', models.DecimalField(decimal_places=0, max_digits=12)),
                ('itlb_cache', models.DecimalField(decimal_places=0, max_digits=12)),
                ('itlb_cache_misses', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
        ),
    ]
