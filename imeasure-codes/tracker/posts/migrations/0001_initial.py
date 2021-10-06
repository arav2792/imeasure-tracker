# Generated by Django 2.0 on 2019-03-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.PositiveSmallIntegerField(default=2019)),
                ('Month', models.CharField(max_length=30)),
                ('Date', models.DateTimeField()),
                ('Shift', models.CharField(max_length=20)),
                ('Day_Of_Week', models.CharField(max_length=20)),
                ('Time', models.TimeField()),
                ('Responded_Time', models.TimeField()),
                ('Time_spent', models.TimeField()),
                ('Complexity', models.CharField(max_length=10)),
            ],
        ),
    ]