# Generated by Django 2.0 on 2019-03-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190312_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='False_alarm',
            new_name='False_Alarm',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Incident_type',
            new_name='Incident_Type',
        ),
        migrations.AddField(
            model_name='post',
            name='Name',
            field=models.CharField(default='Please select', max_length=100, null=True),
        ),
    ]
