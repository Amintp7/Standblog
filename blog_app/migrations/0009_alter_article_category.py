# Generated by Django 5.0.2 on 2024-03-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog_app.category'),
        ),
    ]