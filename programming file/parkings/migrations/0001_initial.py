from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('parking_time', models.FloatField(default=0.0)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lots.Lot')),
            ],
        ),
    ]
