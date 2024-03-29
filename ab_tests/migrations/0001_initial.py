# Generated by Django 3.0.3 on 2020-02-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={'db_table': 'experiments',},
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('probability', models.PositiveIntegerField()),
                (
                    'experiment',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='variations',
                        to='ab_tests.Experiment',
                    ),
                ),
            ],
            options={'db_table': 'variations',},
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idfa', models.CharField(max_length=64)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ab_tests.Variation')),
            ],
            options={'db_table': 'groups',},
        ),
    ]
