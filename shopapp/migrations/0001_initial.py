# Generated by Django 4.2 on 2023-04-06 13:58

from django.db import migrations, models
import django.db.models.deletion
import shopapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shopapp.models.getfilename)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='o-show,1-hidden')),
                ('trending', models.BooleanField(default=False, help_text='o-default,1-Trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shopapp.models.getfilename)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='o-show,1-hidden')),
                ('trending', models.BooleanField(default=False, help_text='o-default,1-Trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.catagory')),
            ],
        ),
    ]