# Generated by Django 4.0.5 on 2022-06-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spamapp', '0002_remove_spammail_mail_body_spammail_email_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spammail',
            name='Email_Body',
            field=models.CharField(default='', max_length=100),
        ),
    ]