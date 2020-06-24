# Generated by Django 3.0.7 on 2020-06-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholethingAPI', '0002_auto_20200610_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='music',
        ),
        migrations.RemoveField(
            model_name='music',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
