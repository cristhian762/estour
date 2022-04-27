# Generated by Django 4.0.3 on 2022-04-19 23:10

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPlace',
            fields=[
                ('id', models.UUIDField(default=places.models.uuid_generator, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='category_place')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(default=places.models.uuid_generator, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.UUIDField(default=places.models.uuid_generator, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('card_img', models.ImageField(blank=True, upload_to='places')),
                ('banner', models.ImageField(blank=True, upload_to='places')),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=14, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=14, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='places.categoryplace')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.UUIDField(default=places.models.uuid_generator, editable=False, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=places.models.uuid_generator, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='gallery_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.gallery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='places.place'),
        ),
    ]
