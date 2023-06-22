# Generated by Django 3.0.2 on 2020-12-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201208_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='idgenerate',
            fields=[
                ('idcard_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('session', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]
