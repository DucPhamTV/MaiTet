# Generated by Django 3.2.4 on 2021-07-18 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20210626_0735'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='tracker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='tracker.tracker'),
        ),
    ]