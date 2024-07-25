# Generated by Django 5.0 on 2024-07-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=800)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
