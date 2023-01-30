# Generated by Django 3.2.8 on 2023-01-30 15:33

from django.db import migrations, models
import django_lifecycle.mixins
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_useraccount_name_changes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
            ],
            options={
                'db_table': 'post',
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]