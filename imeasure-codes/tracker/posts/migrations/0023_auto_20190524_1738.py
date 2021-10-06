# Generated by Django 2.2.1 on 2019-05-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20190518_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(db_column='dete', default='2019-05-24'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Day_Of_Week',
            field=models.TextField(db_column='dayofweek', default='Weekday'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.CharField(db_column='weekno', default='Week 21', max_length=20, null=True),
        ),
    ]
