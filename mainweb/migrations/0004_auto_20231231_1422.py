# Generated by Django 3.2.23 on 2023-12-31 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0003_auto_20231230_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='mainweb.page', verbose_name='Родитель:'),
        ),
    ]
