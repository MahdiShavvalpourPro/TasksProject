from django.db import models

# Create your models here.


class task_status(models.TextChoices):
    COMPLETED = 'CO', 'completed'
    INPROGRESS = 'IN', 'inprogress'
    PENDING = 'PE', 'pending'


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=500, verbose_name='توضحیات')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ ویرایش')
    status = models.CharField(max_length=2, choices=task_status.choices, default=task_status.PENDING,
                              verbose_name='وضعیت')

    class Meta:
        verbose_name: 'وظیفه'
        verbose_name_plural: 'وظایف'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.title}'
