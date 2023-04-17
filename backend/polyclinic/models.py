from django.db import models
from django.utils import timezone


class DoctorsSpecializations(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование специализации доктора"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления специализации"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления специализации"
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'специализацию'
        verbose_name_plural = 'Специализации'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)


class Doctors(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Имя доктора"
    )
    specialization_id = models.ForeignKey(
        DoctorsSpecializations, on_delete=models.SET_NULL,
        null=True, verbose_name="Специализация доктора"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации доктора"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления данных доктора"
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'врача'
        verbose_name_plural = 'Врачи'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)