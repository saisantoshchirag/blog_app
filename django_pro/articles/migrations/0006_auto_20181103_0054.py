# Generated by Django 2.1.1 on 2018-11-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20181103_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]