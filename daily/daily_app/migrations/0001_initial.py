# Generated by Django 5.0.2 on 2024-02-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
