# Generated by Django 3.1.2 on 2021-09-16 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sleep',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='sleep',
            name='hours',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sleeps', to=settings.AUTH_USER_MODEL),
        ),
    ]
