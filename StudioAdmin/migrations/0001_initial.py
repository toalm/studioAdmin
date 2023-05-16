# Generated by Django 4.2.1 on 2023-05-14 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='COL_NAME', default='', max_length=128)),
            ],
            options={
                'db_table': 'T_FEATURE',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='COL_NAME', max_length=128)),
            ],
            options={
                'db_table': 'T_PRODUCT',
            },
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'T_QUOTA',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='COL_NAME', default='', max_length=128)),
                ('type', models.CharField(choices=[('int', 'Number'), ('str', 'Text'), ('bool', 'Toggle')], db_column='COL_TYPE', default='bool', max_length=16)),
                ('feature', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StudioAdmin.feature')),
            ],
            options={
                'db_table': 'T_PARAMETER',
            },
        ),
        migrations.AddField(
            model_name='feature',
            name='products',
            field=models.ManyToManyField(db_column='COL_PRODUCT_ID', related_name='features', to='StudioAdmin.product'),
        ),
    ]