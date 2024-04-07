# Generated by Django 5.0.4 on 2024-04-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('img', models.ImageField(null=True, upload_to='seller_profile_imgs/')),
            ],
        ),
    ]
