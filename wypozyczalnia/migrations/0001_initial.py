# Generated by Django 3.1.4 on 2021-04-27 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AditionalEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'aditional_equipment',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=20)),
                ('rok_produkcji', models.IntegerField()),
                ('cena_za_godzine', models.IntegerField()),
                ('dostepnosc', models.BooleanField(default=True)),
                ('klimatyzacja', models.BooleanField(default=True)),
                ('ilosc_drzwi', models.IntegerField()),
                ('zdjecie', models.ImageField(default='no_image.png', upload_to='cars/%Y/%m/%d')),
            ],
            options={
                'db_table': 'car',
                'ordering': ('model',),
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'fuel_type',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'model',
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1, unique=True)),
            ],
            options={
                'db_table': 'segment',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('text', models.TextField(blank=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ocena',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('power', models.FloatField()),
                ('consumation', models.FloatField()),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engines', to='wypozyczalnia.fueltype')),
            ],
            options={
                'db_table': 'engine',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='wypozyczalnia.model'),
        ),
        migrations.AddField(
            model_name='car',
            name='opcjonalne_wyposazenie',
            field=models.ManyToManyField(related_name='cars', to='wypozyczalnia.AditionalEquipment'),
        ),
        migrations.AddField(
            model_name='car',
            name='segment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='wypozyczalnia.segment'),
        ),
        migrations.AddField(
            model_name='car',
            name='silnik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='wypozyczalnia.engine'),
        ),
    ]
