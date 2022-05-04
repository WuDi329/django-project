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
    cpu_per = models.CharField(max_length=5)
    max_size = models.CharField(max_length=8)
    page_fault = models.CharField(max_length=6)
    mpage_fault = models.CharField(max_length=8)
    elapse_time = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.elf_name + str(self.run_time)

