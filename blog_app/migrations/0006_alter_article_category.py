# Generated by Django 5.0.2 on 2024-03-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_alter_article_options_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='aritecles', to='blog_app.category'),
        ),
    ]
