from djongo import models

class jilu(models.Model):
    name = models.CharField(max_length=200)
    per_time = models.DecimalField(max_digits=12, decimal_places=0)
    call_times = models.DecimalField(max_digits=12, decimal_places=0)
    percent = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        abstract = True

class Straceinfo(models.Model):
    elf_name = models.CharField(max_length=200)
    params = models.CharField(max_length=200, default=" ")
    msg = models.ArrayField(
        model_container= jilu
    )