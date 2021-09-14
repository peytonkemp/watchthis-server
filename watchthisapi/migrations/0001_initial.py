# Generated by Django 3.2.7 on 2021-09-14 15:56

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
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('backdrop_path', models.URLField()),
                ('overview', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.URLField()),
                ('release_date', models.DateField()),
                ('revenue', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('tagline', models.TextField()),
                ('vote_average', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('backdrop_path', models.URLField()),
                ('overview', models.TextField()),
                ('popularity', models.IntegerField()),
                ('poster_path', models.URLField()),
                ('tagline', models.TextField()),
                ('vote_average', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TvGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TvWatchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchthisapi.tv')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchthisapi.watchlist')),
            ],
        ),
        migrations.CreateModel(
            name='MovieWatchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchthisapi.movie')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchthisapi.watchlist')),
            ],
        ),
    ]
