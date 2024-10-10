from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        COMPLETED = 'CO', 'completed'
        PROGRESS = 'IN', 'progress'
        PENDING = 'PE', 'pending'

    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=500, verbose_name='توضحیات')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ ویرایش')
    status = models.CharField(max_length=2, choices=TaskStatus.choices, default=TaskStatus.PENDING,
                              verbose_name='وضعیت')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.title} | Status : {self.status}'
