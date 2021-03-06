# Generated by Django 3.1.7 on 2021-04-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_auto_20210410_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('airCooler', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.aircooler')),
                ('attaChakki', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.attachakki')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
                ('homeTheater', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.hometheater')),
                ('hotplate', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.hotplate')),
                ('iron', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.iron')),
                ('juicerMixer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.juicermixer')),
                ('juicerMixerGrinder', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.juicermixergrinder')),
                ('refrigerator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.refrigerator')),
                ('towerTheater', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.towertheater')),
                ('tv', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.tv')),
            ],
        ),
    ]
