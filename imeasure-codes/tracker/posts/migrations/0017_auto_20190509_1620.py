# Generated by Django 2.0 on 2019-05-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20190508_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Alert',
            field=models.CharField(blank=True, db_column='alertname', default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='General_Health_Check',
            field=models.CharField(blank=True, db_column='ghcname', default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='If_Others_Please_Specify',
            field=models.CharField(blank=True, db_column='others', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Remediation',
            field=models.TextField(blank=True, db_column='remediation', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Task',
            field=models.CharField(blank=True, db_column='taskname', default='NA', max_length=100, null=True),
        ),
    ]
