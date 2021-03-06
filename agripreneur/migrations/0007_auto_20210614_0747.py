# Generated by Django 3.2.4 on 2021-06-14 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agripreneur', '0006_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Consumer', 'Consumer'), ('Farmer', 'Farmer'), ('Small Scale Trader', 'Small Scale Trader'), ('Large Scale Trader', 'Large Scale Trader'), ('Exporter', 'Exporter')], default='Consumer', max_length=50)),
                ('product_category', models.CharField(choices=[('Vegetables', 'Vegetables'), ('Chicken', 'Chicken'), ('Chilli', 'Chilli'), ('Rabbit', 'Rabbit'), ('Spices', 'Spices'), ('Farm Animals', 'Farm Animals'), ('None', 'None')], default='Vegetables', max_length=50)),
                ('product_volume', models.CharField(choices=[('Small Scale', 'Small Scale'), ('Large Scale', 'Large Scale'), ('Export Volume', 'Export Volume'), ('None', 'None')], default='Small Scale', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='location',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='Farmer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
