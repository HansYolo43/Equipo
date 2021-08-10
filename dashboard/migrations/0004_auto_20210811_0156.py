# Generated by Django 3.2.6 on 2021-08-10 20:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_to_do_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='to_do',
            options={'ordering': ['-due_date']},
        ),
        migrations.AddField(
            model_name='to_do',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
