# Generated by Django 2.2.1 on 2019-12-10 11:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('prod_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='subscription_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
