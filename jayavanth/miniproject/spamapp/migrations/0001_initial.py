# Generated by Django 4.0.5 on 2022-06-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spammail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mail_Body', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
