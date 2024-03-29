# Generated by Django 5.0.2 on 2024-02-11 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_app.topico')),
            ],
            options={
                'verbose_name_plural': 'entradas',
            },
        ),
    ]
