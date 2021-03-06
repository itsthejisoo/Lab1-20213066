from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('basic_rate', models.IntegerField(default=0)),
                ('additional_rate', models.IntegerField(default=0)),
                ('time_weekdays', models.CharField(max_length=30, null=True)),
                ('time_weekends', models.CharField(max_length=30, null=True)),
                ('section_count', models.IntegerField(default=0)),
            ],
        ),
    ]
