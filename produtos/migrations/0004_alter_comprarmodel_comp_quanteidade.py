# Generated by Django 4.2.1 on 2023-05-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_comprarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprarmodel',
            name='comp_quanteidade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
