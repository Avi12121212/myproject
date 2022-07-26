# Generated by Django 4.0.4 on 2022-06-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapps', '0007_quiz_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('option_a', models.CharField(max_length=50)),
                ('option_b', models.CharField(max_length=50)),
                ('option_c', models.CharField(max_length=50)),
                ('option_d', models.CharField(max_length=50)),
                ('correct', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
