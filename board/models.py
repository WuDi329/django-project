from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Bintime(models.Model):
    elf_name = models.CharField(max_length=200)
    # the true date when i process
    run_time = models.DateTimeField(auto_now_add=True)
    user_time = models.DecimalField(max_digits=6, decimal_places=3)
    sys_time = models.DecimalField(max_digits=6, decimal_places=3)
    cpu_per = models.DecimalField(max_digits=5, decimal_places=2)
    max_size = models.DecimalField(max_digits=8, decimal_places=0)
    page_fault = models.DecimalField(max_digits=6, decimal_places=0)
    mpage_fault = models.DecimalField(max_digits=8, decimal_places=0)
    elapse_time = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.elf_name + str(self.run_time)

class Elfinfo(models.Model):
    elf_name = models.CharField(max_length=200)
    text_length = models.DecimalField(max_digits=12, decimal_places=0)
    data_length = models.DecimalField(max_digits=12, decimal_places=0)
    bss_length = models.DecimalField(max_digits=12, decimal_places=0)
    dec_length = models.DecimalField(max_digits=12, decimal_places=0)

    def __str__(self):
        return self.elf_name