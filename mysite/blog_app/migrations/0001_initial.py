# Generated by Django 3.2 on 2022-07-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='blog_app')),
                ('activate', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('p', 'publish'), ('d', 'dradt')], default='d', max_length=2)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
