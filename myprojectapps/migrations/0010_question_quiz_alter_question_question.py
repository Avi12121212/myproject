# Generated by Django 4.0.4 on 2022-06-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapps', '0009_remove_question_correct_alter_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myprojectapps.quiz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]
