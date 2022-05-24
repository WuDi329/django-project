from djongo import models

class jilu(models.Model):
    name = models.CharField(max_length=200)
    per_time = models.CharField(max_length=20)
    call_times = models.CharField(max_length=20)
    percent = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Straceinfo(models.Model):
    elf_name = models.CharField(max_length=200)
    params = models.CharField(max_length=200, default=" ")
    msg = models.ArrayField(
        model_container= jilu
    )