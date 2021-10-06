# Generated by Django 2.2 on 2020-03-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20190610_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(db_column='dete', default='2020-03-16'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Month',
            field=models.CharField(db_column='menth', default='March', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Shift',
            field=models.TextField(db_column='shyft', default='EMEA'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.CharField(db_column='weekno', default='Week 12', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Year',
            field=models.PositiveSmallIntegerField(db_column='yeer', default=2020),
        ),
    ]