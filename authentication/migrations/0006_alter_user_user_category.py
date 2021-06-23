# Generated by Django 3.2.4 on 2021-06-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'User'), (2, 'Seller'), (3, 'Dilevery Boy')], default=1),
        ),
    ]
