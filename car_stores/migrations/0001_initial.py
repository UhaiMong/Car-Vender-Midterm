# Generated by Django 4.2.7 on 2024-01-20 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.IntegerField()),
                ('model_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car_stores.brand')),
            ],
        ),
    ]