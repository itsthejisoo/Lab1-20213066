from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='additional_rate',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lot',
            name='basic_rate',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lot',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='lot',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='lot',
            name='section_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lot',
            name='time_weekdays',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lot',
            name='time_weekends',
            field=models.CharField(max_length=30),
        ),
    ]
