# Generated by Django 2.0.6 on 2019-02-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190212_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]