# Generated by Django 5.1.1 on 2024-10-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('CO', 'completed'), ('IN', 'progress'), ('PE', 'pending')], default='PE', max_length=2, verbose_name='وضعیت'),
        ),
    ]
