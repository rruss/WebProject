# Generated by Django 2.2 on 2019-05-12 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190512_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='ok_answer',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Title'),
        ),
    ]