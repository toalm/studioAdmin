# Generated by Django 4.2.1 on 2023-05-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudioAdmin', '0006_remove_feature_products_productfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='products',
            field=models.ManyToManyField(db_column='COL_PRODUCT_ID', related_name='features', to='StudioAdmin.product'),
        ),
        migrations.DeleteModel(
            name='ProductFeature',
        ),
    ]
