# Generated by Django 2.2.1 on 2019-06-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20190531_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(db_column='dete', default='2019-06-05'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Month',
            field=models.CharField(db_column='menth', default='June', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Shift',
            field=models.TextField(db_column='shyft', default='USA'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.CharField(db_column='weekno', default='Week 23', max_length=20, null=True),
        ),
    ]