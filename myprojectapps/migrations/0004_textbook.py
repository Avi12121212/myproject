# Generated by Django 4.0.4 on 2022-05-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapps', '0003_simplebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'textbook',
            },
        ),
    ]
