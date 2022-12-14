# Generated by Django 4.0.6 on 2022-10-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField(default=0.0)),
                ('Maltodextrin', models.FloatField(default=0.0)),
                ('FlowRate', models.FloatField(default=0.0)),
                ('Yield', models.FloatField(blank=True, default=0.0)),
                ('MoistureContent', models.FloatField(blank=True, default=0.0)),
                ('ColorChange', models.FloatField(blank=True, default=0.0)),
                ('R', models.FloatField(blank=True, default=0.0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
