# Generated by Django 4.1.2 on 2022-11-29 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0003_alter_funcionario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]