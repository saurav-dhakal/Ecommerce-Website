# Generated by Django 4.0.2 on 2023-06-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_folder_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=50)),
                ('comment', models.CharField(default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.folder')),
            ],
        ),
    ]
