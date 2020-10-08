# Generated by Django 3.1.2 on 2020-10-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
