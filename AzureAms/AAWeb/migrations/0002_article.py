# Generated by Django 4.1 on 2022-11-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AAWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tomtat', models.CharField(max_length=4000)),
            ],
        ),
    ]
