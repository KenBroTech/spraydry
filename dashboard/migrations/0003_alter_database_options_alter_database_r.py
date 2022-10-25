# Generated by Django 4.0.6 on 2022-10-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_database'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='database',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Data'},
        ),
        migrations.AlterField(
            model_name='database',
            name='R',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Wettability'),
        ),
    ]
