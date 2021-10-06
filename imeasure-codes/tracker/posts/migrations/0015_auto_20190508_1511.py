# Generated by Django 2.0 on 2019-05-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20190502_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Name',
        ),
        migrations.AddField(
            model_name='post',
            name='Alert',
            field=models.CharField(db_column='alertname', default='Please select', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='General_Health_Check',
            field=models.CharField(db_column='ghcname', default='Please select', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Task',
            field=models.CharField(db_column='taskname', default='Please select', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Week',
            field=models.IntegerField(db_column='weekno', default=19, null=True),
        ),
    ]