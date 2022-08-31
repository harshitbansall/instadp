# Generated by Django 4.1 on 2022-08-31 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('searched_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'searched_usernames',
            },
        ),
    ]