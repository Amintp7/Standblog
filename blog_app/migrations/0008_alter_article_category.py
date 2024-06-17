# Generated by Django 5.0.2 on 2024-03-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog_app.category'),
        ),
    ]