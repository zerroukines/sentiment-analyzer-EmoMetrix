# Generated by Django 4.0 on 2023-02-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('sentiment', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='SentimentAnalysisHistory',
        ),
    ]