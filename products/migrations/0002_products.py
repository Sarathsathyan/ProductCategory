# Generated by Django 3.0.8 on 2020-07-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100)),
                ('pro_image', models.ImageField(null=True, upload_to='SubProduct_images/')),
                ('product_price', models.IntegerField()),
                ('produ_features', models.CharField(max_length=500, null=True)),
                ('prod_description', models.CharField(max_length=500)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]
