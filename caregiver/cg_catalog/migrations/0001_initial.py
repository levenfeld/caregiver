# Generated by Django 2.0.4 on 2018-04-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(help_text='Enter here the city name', max_length=128)),
                ('city_state', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapa'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espirito Santo'), ('GO', 'Goias'), ('MA', 'Maranhao'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Para'), ('PB', 'Paraiba'), ('PE', 'Pernambuco'), ('PI', 'Piaui'), ('PR', 'Parana'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondonia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'Sao Paulo'), ('TO', 'Tocantins')], default='', help_text='Choose the city state', max_length=2)),
            ],
            options={
                'ordering': ['city_state', 'city_name'],
            },
        ),
    ]
