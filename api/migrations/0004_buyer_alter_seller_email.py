# Generated by Django 5.0.4 on 2024-04-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
