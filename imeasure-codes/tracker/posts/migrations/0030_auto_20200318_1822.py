# Generated by Django 2.2 on 2020-03-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20200318_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Shift',
            field=models.TextField(db_column='shyft', default='EMEA'),
        ),
    ]
