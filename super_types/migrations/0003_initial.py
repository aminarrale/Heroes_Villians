# Generated by Django 4.0.5 on 2022-06-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('super_types', '0002_delete_supertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]
