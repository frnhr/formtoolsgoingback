# Generated by Django 2.0.1 on 2018-08-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WizardResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_1_1', models.CharField(max_length=254)),
                ('response_1_2', models.CharField(max_length=254)),
                ('response_2_1', models.CharField(max_length=254)),
                ('response_2_2', models.CharField(max_length=254)),
                ('response_3_1', models.CharField(max_length=254)),
                ('response_3_2', models.CharField(max_length=254)),
            ],
        ),
    ]