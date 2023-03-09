# Generated by Django 4.1.7 on 2023-03-08 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0002_destinations'),
    ]

    operations = [
        migrations.CreateModel(
            name='tripdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=50)),
                ('fromdate', models.DateField()),
                ('duration', models.IntegerField()),
                ('tripwith', models.CharField(max_length=20)),
                ('interests', models.CharField(max_length=30)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.profile')),
            ],
        ),
    ]