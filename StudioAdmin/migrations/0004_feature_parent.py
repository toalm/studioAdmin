# Generated by Django 4.2.1 on 2023-05-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudioAdmin', '0003_quota_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='parent',
            field=models.ForeignKey(db_column='COL_PARENT', default=None, on_delete=django.db.models.deletion.CASCADE, to='StudioAdmin.feature'),
        ),
    ]