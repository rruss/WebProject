# Generated by Django 2.2 on 2019-05-12 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_ok_answer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ok_answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question'),
        ),
        migrations.AlterField(
            model_name='ok_answer',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='okanswers', to='api.Title'),
        ),
    ]